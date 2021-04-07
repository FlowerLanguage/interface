#!/root/miniconda3/envs/myenv/bin/python
from aiohttp import ClientSession
import re
import asyncio
import logging
import requests
import time
import pandas as pd
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[Line：%(lineno)d] - %(levelname)s %(message)s',
                    filename='/home/interface/fixed/Logs/foreign_currency.txt',
                    filemode='a')
session = None
CURRENCY = 4
semaphore = asyncio.Semaphore(CURRENCY)


def get_foreign_currency_type():
    """
    获取当前
    """
    url = 'https://cn.investing.com/currencies/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Cookies': 'adBlockerNewUserDomains=1606294439; __gads=ID=6b57c5bf63ac5b10:T=1606294443:S=ALNI_MbYmfzMLtICWJssMRSActIuNLKDzw; _ga=GA1.2.1394063966.1606294442; __atuvc=7%7C48; PHPSESSID=qivi63qfb7aej5hip27ks76c0b; geoC=CN; StickySession=id.16411847798.287cn.investing.com; logglytrackingsession=e633f82b-ca39-4c60-bd70-880e4e92103e; _gid=GA1.2.1781600672.1610501194; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1607999653,1610501202; adsFreeSalePopUp=3; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A7%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22166%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Findices%2Fus-spx-500%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2244336%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fvolatility-s-p-500%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22179%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Findices%2Fhang-sen-40%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2240820%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fshanghai-composite%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226377%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fsina-corp%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222111%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A16%3A%22%E7%BE%8E%E5%85%83+%E4%BA%BA%E6%B0%91%E5%B8%81%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-cny%22%3B%7Di%3A6%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22942611%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A17%3A%22%2Findices%2Fusdollar%22%3B%7D%7D%7D%7D; outbrain_cid_fetch=true; nyxDorf=NjI2Z2IxM3E2Z25iYy4zM2M7YyZhZ2dk; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+13+2021+10%3A08%3A50+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BBJ; OptanonAlertBoxClosed=2021-01-13T02:08:50.780Z; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1610503731'
    }
    res = requests.get(url, headers=headers)
    res = re.findall('<table id=".*?" tablesorter class=".*?">(.*?)</table>', res.text, re.S)[0]
    trs = re.findall('<tr id="(.*?)>(.*?)</tr>', res, re.S)
    types = []
    for tr in trs:
        curr_id = tr[0].split('_')[1][0:-1]
        header = re.findall('<td class="left noWrap">(.*?)</td>', tr[1], re.S)[0]
        types.append((curr_id, header))
    return types


def get_date():
    """
    获取当前日期
    """
    date = time.strftime('%Y/%m/%d', time.localtime())
    # date = '2021/01/12'
    return date


async def get_data(start_date=get_date(), end_date=get_date(), param=None):
    url = 'https://cn.investing.com/instruments/HistoricalDataAjax'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Cookies': 'adBlockerNewUserDomains=1606294439; __gads=ID=6b57c5bf63ac5b10:T=1606294443:S=ALNI_MbYmfzMLtICWJssMRSActIuNLKDzw; _ga=GA1.2.1394063966.1606294442; __atuvc=7%7C48; PHPSESSID=qivi63qfb7aej5hip27ks76c0b; geoC=CN; StickySession=id.16411847798.287cn.investing.com; logglytrackingsession=e633f82b-ca39-4c60-bd70-880e4e92103e; _gid=GA1.2.1781600672.1610501194; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1607999653,1610501202; adsFreeSalePopUp=3; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A7%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22166%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Findices%2Fus-spx-500%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2244336%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fvolatility-s-p-500%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22179%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Findices%2Fhang-sen-40%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2240820%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fshanghai-composite%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226377%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fsina-corp%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222111%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A16%3A%22%E7%BE%8E%E5%85%83+%E4%BA%BA%E6%B0%91%E5%B8%81%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-cny%22%3B%7Di%3A6%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22942611%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A17%3A%22%2Findices%2Fusdollar%22%3B%7D%7D%7D%7D; outbrain_cid_fetch=true; nyxDorf=NjI2Z2IxM3E2Z25iYy4zM2M7YyZhZ2dk; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+13+2021+10%3A08%3A50+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BBJ; OptanonAlertBoxClosed=2021-01-13T02:08:50.780Z; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1610503731',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'curr_id': param[0],
        'smIID': '',
        'header': param[1] + '历史数据',
        'st_date': start_date,
        'end_date': end_date,
        'interval_sec': 'Daily',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical-data'
    }
    async with semaphore:
        async with session.post(url, headers=headers, data=data) as res:
            res = await res.text()
            res = re.findall('<tbody>(.*?)</tbody>', res, re.S)[0].strip()
            tds = re.findall('<td .*?>(.*?)</td>', res, re.S)
            date = start_date.replace('/', '-')  # 日期
            close = float(tds[1])  # 闭盘
            open = float(tds[2])  # 开盘
            high = float(tds[3])  # 最高价
            low = float(tds[4])  # 最低价
            net_chg_pct = float(tds[5][0:-1]) * 0.01  # 涨跌幅
            symbol = param[1].replace('/', '-')  # 外汇类型
            return [date, close, open, high, low, net_chg_pct, symbol]


def post_data(data):
    """
        post请求，将获取的值，直接发送给服务器
        """
    headers = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    url = 'http://60.205.201.200/foreign_currency/'  # 服务器外汇数据地址
    df = pd.DataFrame(data)
    df.columns = ['date', 'close', 'open', 'high', 'low', 'net_chg_pct', 'symbol']
    print(df.dtypes)  # 获取df对象每个列的数据类型
    logging.info('data have {}kb!'.format(sys.getsizeof(df) / 1024.))  # 获取df对象的大小,kb为单位
    print(df.describe())  # 查看爬取的数据的总体信息·
    data = df.to_json(orient='records')  # 将dataframe对象转换为json
    print(requests.post(url, data=data, headers=headers))  # 发送data数据给服务器


async def dispatch_tasks():
    logging.info('start get foreign_currency types!')
    types = get_foreign_currency_type()
    logging.info('end get foreign_currency types!')

    logging.info('start get foreign_currency data!')
    global session
    session = ClientSession()
    tasks = [asyncio.ensure_future(get_data(param=i)) for i in types]
    results = await asyncio.gather(*tasks)
    await session.close()
    logging.info('end get foreign_currency data!')

    logging.info('start post foreign_currency data!')
    post_data(results)
    logging.info('end post foreign_currency data!')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(dispatch_tasks())
