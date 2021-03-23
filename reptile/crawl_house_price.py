import time
import requests
import re
import pandas as pd
import logging
import sys


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filename="Logs/house.txt",
                    filemode='a')


def ge_data():
    """
    根据目标网站获取当月全国各城市的相关信息，返回年份，月份和包含信息的列表
    :return: 年，月，数据信息
    """
    logging.info('start get city information!')
    url = 'https://www.creprice.cn/rank/cityforsale.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    res = requests.get(url, headers=headers).text

    date = re.findall('<h1 class="tith">.*?</span>(.*?)</h1>', res, re.S)[0]  # 提取此次请求日期，格式(2021年02月全国城市住宅房价排行榜)
    year = date.split('年')[0]  # 提取年份
    month = (date.split('年')[1]).split('月')[0]  # 提取月份

    data = re.findall('<tbody class="ranklist">(.*?)</tbody>', res, re.S)[0]  # 找到所有城市的父类tbody
    trs = re.findall('<tr onclick=".*?" style=".*?">(.*?)</tr>', data, re.S)  # 找到所有电影对应的所有tr，一个tr即为一个电影信息
    results = []  # 用于存储提取的城市信息
    for tr in trs:
        th1 = re.findall('<th>(.*?)</th>', tr, re.S)  # 包含城市名和平均单价(元/㎡)
        th2 = re.findall('<th .*?>(.*?)</th>', tr, re.S)  # 包含环比和同比

        city = re.findall('<a .*?>(.*?)</a>', th1[1], re.S)[0].strip()  # 城市
        avg_unit_price = th1[2].replace(',', '')  # 平均单价
        chain_comparison = th2[0]  # 环比
        year_on_year = th2[1]  # 同比
        results.append([city, avg_unit_price, chain_comparison, year_on_year])
    logging.info('end get city information!')
    return year, month, results


def post_data(params):
    """
    根据传来的参数，发送数据到服务器
    :param params:包含年，月，城市信息
    """
    logging.info('start post data!')
    print(params[0])
    print(params[1])
    df = pd.DataFrame(params[2])
    df.columns = ['city', 'avg_unit_price', 'chain_comparison', 'year_on_year']
    data = df.to_json(orient='records')
    logging.info('data size is {}kb!'.format(sys.getsizeof(data)/1024.))
    print(data)

    
    logging.info('end post data!')


def dispatch():
    """
    调度函数，安排整个文件个函数的执行逻辑
    """
    logging.info('start function!')
    year, month, data = ge_data()  # 调用获取信息的相关函数
    post_data([year, month, data])  # 调用发送数据的相关函数


if __name__ == '__main__':
    dispatch()
