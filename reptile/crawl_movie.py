import requests
import re
import logging
import time
import json
import pandas as pd
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s",
                    filename='Logs/movie.txt',
                    filemode='a')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookies': '_lxsdk_cuid=17833761240c8-0a1827390dd80a-5771133-144000-1783376124054; _lxsdk=17833761240c8-0a1827390dd80a-5771133-144000-1783376124054; __mta=213284779.1615773194112.1616062062195.1616073872305.53; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1784821918e-82e-759-809%7C%7C4'

}


def get_all_year():
    """
    获取网页上显示的所有年份的url请求地址,分两部分，一部分为当年和全部；另一部分为以前的年份
    :return: 返回提取的所有年份的URL,分成两部分.以前已经不可变的年份previous_years;以及可变的variable_year
    """
    logging.info('start get all years_url!')
    url = 'http://piaofang.maoyan.com/mdb/rank'  # 主站

    res = requests.get(url, headers=headers)
    res = res.text
    res = re.findall('<ul class="h-tabs">(.*?)</ul>', res, re.S)[0]  # 首先提取出包含所有年份的所有标签，一个列表元素
    res = re.findall('<li .*?>(.*?)</li>', res, re.S)  # 提取找到所有的年份

    this_year = time.strftime('%Y', time.localtime())  # 获取当前日期的年份
    previous_years = []  # 用来存储网页上找到的以前的年份对应板块的Ajax目标地址
    variable_year = []  # 用来存储网页上找到的现在的年份以及全部板块的Ajax目标地址

    url_data = 'http://piaofang.maoyan.com/mdb/rank/query?type=0&id={}'  # 基础的Ajax请求地址
    for i in res:
        if i == '全部':
            variable_year.append(url_data.format(0))
        elif i == this_year:
            variable_year.append(url_data.format(this_year))
        else:
            previous_years.append(url_data.format(int(float(i))))
    return previous_years, variable_year


def get_movie_simply(year_url):
    """
    提权当年所有电影的简要信息；提权当年所有电影的所有Ajax请求地址
    :param year_url: 单独一年的Ajax请求URL
    :return: simple_movies当年所有电影的简要信息;movie_url当年所有电影的详情URL
    """
    logging.info('start get movie information({})'.format(year_url))
    res = requests.get(year_url, headers=headers).text  # 取得Ajax请求的内容
    res = json.loads(res)  # 将返回的json格式转换为python内部的数据类型
    res = res['data']['list']  # 获取到当年所有电影的一个对象
    base_url = 'http://piaofang.maoyan.com/movie/{}'  # 电影基本的url，需要获取电影的movieID进行组合

    simple_movies = []  # 用来存储所有电影的简单信息
    movie_urls = []  # 用来存储所有电影的详细网页地址

    for j in res:
        movie_urls.append(base_url.format(j['movieId']))  # 提取拼接成电影详情页的URL
        name = j['movieName']  # 电影名
        box = j['boxDesc']  # 票房
        avg_fare = j['avgViewBoxDesc']  # 平均票价
        avg_players = j['avgShowViewDesc']  # 场均人次
        url = base_url.format(j['movieId'])
        simple_movies.append([name, box, avg_fare, avg_players, url])  # 将提取的所有电影的信息组合成双重列表
    logging.info('end get movie information!')
    return simple_movies, movie_urls


def get_movie_details(url):
    """
    后续有空，需要解密猫眼的字符串加密方式,现暂不处理
    """
    header1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'http://piaofang.maoyan.com/mob/rank'
    }
    res = requests.get(url, headers=header1).text
    print(res)


def get_and_post(year_url):
    """
    传入需要爬取的年份url，调用get_movie_simply，获取电影信息，并发送到服务器
    """
    headers2 = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    for i in year_url:
        year = i.split('id=')[1]  # 提取爬取的年份具体数字
        if year == '0':
            year = 'whole'  # 目标网站作了替换，全部对应的是id=0.因此需改成和自己服务器上对应的目标地址，改为whole

        post_url = "http://60.205.201.200/movie/{}/".format(year)  # 根据年份构造对应的服务器地址

        simple, detail_urls = get_movie_simply(i)  # 调用函数获取当年所有电影简要信息以及每个电影的详情页

        data = pd.DataFrame(simple)  # 将提取的列表转换为DataFrame对象，方便转换

        data.columns = ['name', 'box', 'avg_fare', 'avg_players', 'url']  # 更改列名
        data['box'][data['box'] == '-'] = 0  # 网站上可能存在一些字段没有数据，显示为-，需要处理替换为0
        data['avg_fare'][data['avg_fare'] == '-'] = 0
        data['avg_players'][data['avg_players'] == '-'] = 0
        data['avg_players'][data['avg_players'] == '-'] = 'http://piaofang.maoyan.com/movie/344264'
        data = data.to_json(orient='records')  # 转换为字典

        logging.info('start post movie({}) data!'.format(year))

        res = requests.post(post_url, headers=headers2, data=data)
        print(res)
        logging.info('post result information is {}!'.format(res))

        logging.info('data size is {}kb!'.format(sys.getsizeof(data) / 1024.))

        logging.info('end post movie data!')


def dispatch():
    """
    调度函数，安排当前文件的执行逻辑
    """
    logging.info('start function!')
    old, new = get_all_year()  # 根据主站获取所有年份
    get_and_post(old)  # 提取并发送以前固定的年份的数据(运行一次即可)
    get_and_post(new)  # 提取并发送可变的，包括当年以及全部电影信息(后期需要实时更新)
    logging.info('end function!')


if __name__ == '__main__':
    dispatch()
