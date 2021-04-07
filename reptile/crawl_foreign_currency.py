from bs4 import BeautifulSoup
import pandas as pd
import os
import asyncio
import aiohttp
import logging
from aiomysql import create_pool
import sys
import requests

CURRENCY = 4  # 最大并发数量
semaphore = asyncio.Semaphore(CURRENCY)  # 生成信号量
semaphore1 = asyncio.Semaphore(1)
session = None
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line: %(lineno)d] - %(levelname)s %(message)s',
                    filename='Logs/foreign_currency.txt',
                    filemode='a')
df = pd.DataFrame()


async def get_foreign_type():
    """
    根据主页，获取有多少中外汇类型
    :return: 列表嵌套列表，列表内容包含Ajax请求所必须的信息
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Cookie': 'adBlockerNewUserDomains=1606294439;'
                  ' __gads=ID=6b57c5bf63ac5b10:T=1606294443:S=ALNI_MbYmfzMLtICWJssMRSActIuNLKDzw;'
                  ' _ga=GA1.2.1394063966.1606294442; _gid=GA1.2.1272127958.1606294444; adsFreeSalePopUp=3;'
                  ' __atuvc=3%7C48; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%'
                  '22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%'
                  '3A2%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%'
                  '3Bs%3A13%3A%22%E6%AC%A7%E5%85%83+%E7%BE%8E%E5%85%83%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%'
                  '2Fcurrencies%2Feur-usd%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226597%22%3Bs%'
                  '3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2'
                  'Frio-tinto%22%3B%7D%7D%7D%7D; PHPSESSID=asmf2290sn9t4fvmka92utct9q; geoC=CN; prebid_session=0; '
                  'StickySession=id.50437178081.504cn.investing.com; logglytrackingsession=74dfa97f-a715-4d81-bf70-c5130399dbe8;'
                  ' Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1606294445,1606353644; prebid_page=0; outbrain_cid_fetch=true;'
                  ' OptanonAlertBoxClosed=2020-11-26T03:09:08.397Z; nyxDorf=MDQ3ZjVmP300ZT0xYi8zMjJjYyZjZWBkYGE%3D;'
                  ' OptanonConsent=isIABGlobal=false&datestamp=Thu+Nov+26+2020+11%3A09%3A09+GMT%'
                  '2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&'
                  'landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&'
                  'AwaitingReconsent=false&geolocation=CN%3BBJ; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1606360150'
    }
    url_home = 'https://cn.investing.com/currencies/'  # 主页
    session = aiohttp.ClientSession()
    res = await session.get(url_home, headers=headers)
    res = await res.text()
    res = BeautifulSoup(res, 'html.parser')
    table = res.find('table', class_='genTbl closedTbl crossRatesTbl')
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    foreign_type_list = []
    for i in trs:
        curr_id = i['id'].split('_')[1]
        foreign_type = i.find_all('td')[2].text
        foreign_type_list.append([curr_id, foreign_type])
    await session.close()
    return foreign_type_list


def solve_time(date_time):
    """
    处理日期格式
    :param date_time: 需要处理的日期字符串
    :return: 返回处理后的日期格式
    """
    date_time = list(date_time)  # 将字符串转换为列表
    date_time.insert(4, '/')  # 4号位插入/
    date_time.insert(7, '/')  # 7号位插入/
    date_time = ''.join(date_time)  # 将列表转换为字符串
    return date_time


async def get_foreign_exchane(start_date='20050101', end_date='20210406', detail_param=None):
    """
    获取外汇数据
    :param detail_param: 一个包含curr_id,以及header的列表，必传
    :param start_date: 开始日期
    :param end_date: 结束日期
    :return: 无返回，调用保存文件的函数
    """
    url = 'https://cn.investing.com/instruments/HistoricalDataAjax'  # 根据网站观察所得出来的Ajax请求目标网址

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Cookie': 'adBlockerNewUserDomains=1606294439;'
                  ' __gads=ID=6b57c5bf63ac5b10:T=1606294443:S=ALNI_MbYmfzMLtICWJssMRSActIuNLKDzw;'
                  ' _ga=GA1.2.1394063966.1606294442; _gid=GA1.2.1272127958.1606294444; adsFreeSalePopUp=3;'
                  ' __atuvc=3%7C48; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%'
                  '22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%'
                  '3A2%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%'
                  '3Bs%3A13%3A%22%E6%AC%A7%E5%85%83+%E7%BE%8E%E5%85%83%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%'
                  '2Fcurrencies%2Feur-usd%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226597%22%3Bs%'
                  '3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2'
                  'Frio-tinto%22%3B%7D%7D%7D%7D; PHPSESSID=asmf2290sn9t4fvmka92utct9q; geoC=CN; prebid_session=0; '
                  'StickySession=id.50437178081.504cn.investing.com; logglytrackingsession=74dfa97f-a715-4d81-bf70-c5130399dbe8;'
                  ' Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1606294445,1606353644; prebid_page=0; outbrain_cid_fetch=true;'
                  ' OptanonAlertBoxClosed=2020-11-26T03:09:08.397Z; nyxDorf=MDQ3ZjVmP300ZT0xYi8zMjJjYyZjZWBkYGE%3D;'
                  ' OptanonConsent=isIABGlobal=false&datestamp=Thu+Nov+26+2020+11%3A09%3A09+GMT%'
                  '2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&'
                  'landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&'
                  'AwaitingReconsent=false&geolocation=CN%3BBJ; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1606360150',
        'X-Requested-With': 'XMLHttpRequest'
    }
    start_date = solve_time(start_date)
    end_date = solve_time(end_date)
    curr_id = detail_param[0]
    header = detail_param[1]
    path = os.getcwd() + '\\results\\' + header.replace('/', '-') + '.csv'  # 文件路径，以及文件名
    data = {
        'curr_id': '{}'.format(curr_id),
        'smIID': '',
        'header': '{}'.format(header),
        'st_date': '{}'.format(start_date),
        'end_date': '{}'.format(end_date),
        'interval_sec': 'Daily',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
    }
    async with semaphore:
        async with session.post(url, headers=headers, data=data) as response:
            await asyncio.sleep(1)
            text = await response.text()  # 获取网页请求的数据
            await get_data(text, path)  # 调用解析数据的函数


async def dispatch_tasks(foeign_types):
    """
    调度函数，建立session,建立任务，任务阻塞，关闭会话
    :param foeign_types: 外汇类型
    :return:
    """
    global session
    session = aiohttp.ClientSession()  # 创建一个session客户端，异步所有请求都需通过这个对象发送
    get_data_tasks = [asyncio.ensure_future(get_foreign_exchane(detail_param=foreign_type)) for foreign_type in
                      foeign_types]  # 创建的协程对象任务集
    await asyncio.gather(*get_data_tasks)  # 协程等待任务执行
    await session.close()


async def get_data(html, path):
    """
    将得到的数据处理保存在全局变量df中
    :param html:网页获取的源码，已转发为text()
    :param path:文件保存路径
    :return:无返回，直接保存数据
    """
    res = BeautifulSoup(html, 'html.parser')
    tbodys = res.find_all('tbody')
    data_body = tbodys[0]
    datas = data_body.find_all('tr')
    data_list = []
    for i in datas:
        data_dict = dict()
        tds = i.find_all('td')
        text = tds[0].text
        text = text.replace('年', '-')  # 替换日期中的年月日
        text = text.replace('月', '-')
        text = text.replace('日', '')
        data_dict['date'] = text  # 日期
        data_dict['close'] = float(tds[1].text)  # 收盘
        data_dict['open'] = float(tds[2].text)  # 开盘
        data_dict['high'] = float(tds[3].text)  # 高
        data_dict['low'] = float(tds[4].text)  # 低
        data_dict['net_chg_pct'] = float(tds[5].text.replace('%', '')) / 100  # 涨幅度
        data_list.append(data_dict)  # 将每天的数据打包成字典，用列表保存
    df1 = pd.DataFrame(data_list)  # 将列表保存为DataFrame对象
    # type1 = path.split('\\')[4].split('.')[0]
    type1 = path.split('.')[0].split('\\')[-1]
    df1['symbol'] = type1
    global df
    df = df.append(df1)  # 添加外汇数据到全局变量df中
    await asyncio.sleep(1)


def post_data():
    """
    post请求，将全局变量的值，直接发送给服务器
    """
    headers = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    url = 'http://60.205.201.200/foreign_currency/'  # 服务器外汇数据地址
    global df  # 引用全局变量
    print(df.dtypes)  # 获取df对象每个列的数据类型
    print(sys.getsizeof(df) / 1024.)  # 获取df对象的大小,kb为单位
    print(df.describe())  # 查看爬取的数据的总体信息·
    logging.info('post data {}kb!'.format(sys.getsizeof(df) / 1024.))
    data = df.to_json(orient='records')  # 将dataframe对象转换为json
    print(requests.post(url, data=data, headers=headers))  # 发送data数据给服务器


async def asyncio_link_database():
    """
    异步连接数据库，直接插入数据
    """
    loop = asyncio.get_event_loop()
    async with create_pool(
            host='116.63.175.23',
            port=3306,
            user='root',
            password='mssdk@028',
            db='mssdk',
            loop=loop
    ) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql_create_table = "CREATE TABLE mssdk_foreign (id int NOT NULL AUTO_INCREMENT,mdate date NOT NULL,mclosing decimal(10,4) NOT NULL,mopening decimal(10,4) NOT NULL,mheight decimal(10,4) NOT NULL,mlow decimal(10,4) NOT NULL,mupanddownrange decimal(10,4) NOT NULL,mtype varchar(20) NOT NULL,PRIMARY KEY (id)) ;"
                await cur.execute(sql_create_table)
                sql_insert = "insert into mssdk_foreign (mdate,mclosing,mopening,mheight,mlow,mupanddownrange,mtype) values(%s,%s,%s,%s,%s,%s,%s);"
                global df
                data = [tuple(row) for row in df.values]
                await cur.executemany(sql_insert, data)
                await conn.commit()


def dispatch_foreign_currency():
    """
    总的调度函数，控制爬取外汇的逻辑
    """
    logging.info('Start scrapping')
    foeign_type = asyncio.get_event_loop().run_until_complete(get_foreign_type())  # 调用获取外汇类型的函数，获取到有多少种外汇类型
    asyncio.get_event_loop().run_until_complete(dispatch_tasks(foeign_type))  # 根据外汇类型函数的结果，进行总事件循环
    logging.info('End scrapping')

    logging.info('start post foreign_currency!')
    post_data()  # 调用保存数据的函数
    logging.info('end post foreign_currency!')


if __name__ == '__main__':
    dispatch_foreign_currency()
