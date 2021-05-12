from bs4 import BeautifulSoup
import pandas as pd
import os
import asyncio
import aiohttp
import logging
from aiomysql import create_pool
import sys
import requests
import time

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
        ':authority':'cn.investing.com',
        ':method':'POST',
        ':path':'/currencies/?__cf_chl_jschl_tk__=e4467bc82526382b890757ad35ee1fcc6978280a-1620781201-0-ASG_8fK24vVLqVFnL4IZykOo85SK1sDogAZrPteitUjk9TNnV10S6gy1dwCSouB00Z1WxE8M7dbiTwZf2_50Odu3mFsNCeW1RX8sGZPVo3XQ7EpFj7eAE33cOxjmSkwhq13A_XMSi3znY11Ow57Rm6X6oUt4A2f-_JMeSkSEFkOonUJupFkgpczojcQU65LLLzbmkiHDsS6snpss8W7zKaxjUHPyJpXFVIuvBU7rfWJbpmn0lKnrvF0Kz8J37KedIEnZnqY5oTD4HY2zpkEZEGlR5QLka2gyrkOlqtrr91ZOPMhvVszPN1lYs5TtticDEFyP6wJfveqOufh044GbYetf-SqOQSBHlfqMcZMU_u8L5SsiY1f_QrtJTLJWZdJGAuiTWqShzbUstpDkMOUJBa2yfSC5nxd2yAMN8JWhCnNlEHJGgrlWBcOSIRX1PIKER42chsjcjBeZnCNUmWyXKA8',
        ':scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cache-control':'max-age=0',
        # 'content-length':'6423',
        'content-type':'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Cookie': 'logglytrackingsession=22d81f2c-dbfa-490d-b05f-14de25c10994; adBlockerNewUserDomains=1606294439; __gads=ID=6b57c5bf63ac5b10:T=1606294443:S=ALNI_MbYmfzMLtICWJssMRSActIuNLKDzw; _ga=GA1.2.1394063966.1606294442; OptanonAlertBoxClosed=2021-01-15T07:47:21.720Z; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jan+15+2021+15%3A47%3A22+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BBJ; protectedMedia=2; __cfduid=d98a47af86e5c7c519900492ce96a7b541620032509; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A13%3A%22%E6%AC%A7%E5%85%83+%E7%BE%8E%E5%85%83%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-usd%22%3B%7D%7D%7D%7D; udid=41f4be753526fed9d24774cf30efda17; PHPSESSID=iajn9bv4stgjm7tl02s3r86aal; geoC=CN; StickySession=id.52744849427.797.cn.investing.com; smd=41f4be753526fed9d24774cf30efda17-1620779168; __cflb=0H28uxmf5JNxjDUC5huTKPtuPTatseegWCS6xNrnoqv; _gid=GA1.2.1454722383.1620779169; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1620779169; adsFreeSalePopUp=3; cf_chl_2=84d6ae6891022c8; cf_chl_prog=x11; cf_clearance=8b05a2be4fa00d6c81ce97deb67e62dcd2b83985-1620781206-0-150; nyxDorf=MzcwYTJhPnxiMz4yN3o3N2czP2AyKzE1Zm8%3D; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1620781206; __cf_bm=c4fd05520ca966541ed69d65789c5c13511ea138-1620781208-1800-AYq/kwqDsq4wBbOZ0vtSKzsU18sMxnx/TP+VtQPzuEfidmm35BAJt0PjPmUP9PipsSSN5H15LIHfrwDuovjLYsO5prQLUlfSZeriAsbPY3RZcdbJenDWw8Uv3oVMmU8mJA==; _gat_allSitesTracker=1',
        'origin':'https://cn.investing.com',
        'referer':"https://cn.investing.com/currencies/?__cf_chl_jschl_tk__=e7716ac8f97621e614d767fda19f140e49256105-1620779163-0-AR4NWD1ADSXX0JWtk29i_qifjHjIwt7kFgrcVtsTw7vGOYzZ32YJLWRARsw4de5reR28eBkiOLtFBmkuZPHne-jb-LrsfwuUhGgn2Wnf2Fu996H_tJ6waYUYzadg_KIsWzoa2-ca0LhcFeCha0F86jq9h_HpBYJvc7tP0UhhNgO1pR1XDqTqU_gSsYSN1pYl60cZ5SSvbsgPxQlho_16-SUQra9z6LgpZD8GTNr64qaezrCTjnehoYPkV8iYXo7KPTga4cIv8Lp_jdbw8GCHF_BELr4YIWoZrAPLibKi1t-6eAcZGR14ulJr75QEiAz5gcOXbliXGWTd76oWFFxXlRl3n5izneQEJGWHXzuK745nyKXdWaXLBjYHfpEsZaIYOWDhTxHQGad-5yoLgsBUnhA3fVmijfcgQTY69--0xUylAAglVYwY5BPFmjLm66u1OuPKKR0ax0xdz-_nG4vlR5I",
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile':'?0',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'same-origin',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1'
    }
    params={
        '__cf_chl_jschl_tk__':'e4467bc82526382b890757ad35ee1fcc6978280a-1620781201-0-ASG_8fK24vVLqVFnL4IZykOo85SK1sDogAZrPteitUjk9TNnV10S6gy1dwCSouB00Z1WxE8M7dbiTwZf2_50Odu3mFsNCeW1RX8sGZPVo3XQ7EpFj7eAE33cOxjmSkwhq13A_XMSi3znY11Ow57Rm6X6oUt4A2f-_JMeSkSEFkOonUJupFkgpczojcQU65LLLzbmkiHDsS6snpss8W7zKaxjUHPyJpXFVIuvBU7rfWJbpmn0lKnrvF0Kz8J37KedIEnZnqY5oTD4HY2zpkEZEGlR5QLka2gyrkOlqtrr91ZOPMhvVszPN1lYs5TtticDEFyP6wJfveqOufh044GbYetf-SqOQSBHlfqMcZMU_u8L5SsiY1f_QrtJTLJWZdJGAuiTWqShzbUstpDkMOUJBa2yfSC5nxd2yAMN8JWhCnNlEHJGgrlWBcOSIRX1PIKER42chsjcjBeZnCNUmWyXKA8'
    }
    data={
        'r':'ebaf707827755372e9662623b0710e7488ad36cf-1620781201-0-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',
        'jschl_vc':'c817f70518c42bb4b36a1d578af9a40a',
        'pass':'1620781205.492-D03PC7tyUr',
        'jschl_answer':'BrvsoAErpjEJ-11-64dfb52d39e33b15',
        'cf_ch_verify':'plat'
    }
    url_home = 'https://cn.investing.com/currencies/'  # 主页
    session = aiohttp.ClientSession()
    await session.post(url_home, headers=headers)
    res = await session.post(url_home, headers=headers,params=params,data=data)
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
    print(foreign_type_list)
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
        ':authority': 'cn.investing.com',
        ':method': 'POST',
        ':path': '/instruments/HistoricalDataAjax',
        ':scheme': 'https',
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
        'X-Requested-With': 'XMLHttpRequest',
        'origin': 'https://cn.investing.com',
        'referer': "https://cn.investing.com/currencies/eur-usd-historical-data",
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
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
            print(text)
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
    df.to_csv('foreign_currency.csv',index=True,encoding='utf-8')
    # print(requests.post(url, data=data, headers=headers))  # 发送data数据给服务器


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
    foreign_type = asyncio.get_event_loop().run_until_complete(get_foreign_type())  # 调用获取外汇类型的函数，获取到有多少种外汇类型

    asyncio.get_event_loop().run_until_complete(dispatch_tasks(foreign_type))  # 根据外汇类型函数的结果，进行总事件循环
    logging.info('End scrapping')

    logging.info('start post foreign_currency!')
    post_data()  # 调用保存数据的函数
    logging.info('end post foreign_currency!')


if __name__ == '__main__':
    dispatch_foreign_currency()
