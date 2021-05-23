import requests
import time
from lxml import etree
import json
import logging
import pandas as pd
import asyncio
import aiohttp

session = None
semaphore = asyncio.Semaphore(4)  # 最大并发量

MUSIC = []
DANCE = []
GAME = []
KNOWLEDGE = []
DIGITAL = []
CAR = []
LIFE = []
FOOD = []
ZOO = []
ENTERTAINMENT = []
MOVIES = []

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s Line[%(lineno)d] %(message)s")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Cookies': "CURRENT_FNVAL=80; _uuid=A7D3D2D6-1811-75C5-8F17-F3414DED8BB437465infoc; blackside_state=1; rpdid=|(Yulukm)lm0J'uY|RRuYlRu; sid=b0z0tsg4; DedeUserID=38836094; DedeUserID__ckMd5=aa9a77fcbb1f8dfb; SESSDATA=0ea875ad%2C1622357180%2C29d6d*c1; bili_jct=349c112ef5644e9f42dad8a09e848a4f; LIVE_BUVID=AUTO6016093965651028; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1609417407; buvid3=2332A819-F381-4003-9461-C8B0A5FAE225185007infoc; fingerprint=82150c9f9418c38d68d6d84db0b4e366; buvid_fp=2332A819-F381-4003-9461-C8B0A5FAE225185007infoc; buvid_fp_plain=3FF81D49-1780-4773-B92F-ADAA7FABE332155821infoc; PVID=5; bsource=search_baidu",
}


def set_session():
    global session
    session = aiohttp.ClientSession()


def get_all_urls():
    """
    获取音乐、舞蹈、游戏、知识、数码、汽车、生活、美食、动物圈、娱乐、影视所有分类下的所有视频
    """
    results = []  # 用来存储最后的url
    url = [
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=3&type=all',  # 音乐
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=129&type=all',  # 舞蹈
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=4&type=all',  # 游戏
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=36&type=all',  # 知识
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=188&type=all',  # 数码
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=223&type=all',  # 汽车
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=160&type=all',  # 生活
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=211&type=all',  # 美食
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=217&type=all',  # 动物圈
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=5&type=all',  # 娱乐
        'https://api.bilibili.com/x/web-interface/ranking/v2?rid=181&type=all'  # 影视
    ]

    columns = ['MUSIC', 'DANCE', 'GAME', 'KNOWLEDGE', 'DIGITAL', 'CAR', 'LIFE', 'FOOD', 'ZOO', 'ENTERTAINMENT',
               'MOVIES']
    for i in url:
        res = requests.get(i)
        response = res.text
        response = json.loads(response)
        index = url.index(i)
        data = response['data']['list']
        for j in data:
            results.append([j['short_link'], columns[index]])
    logging.info('video have {} 个.'.format(len(results)))
    return results


def get_detail(params):
    """
    用来提取每个视频下的详细信息(视频标题,视频作者,发布时间,播放量,弹幕数量,视频分类,点赞数,投币数,收藏数,转发数,视频地址)
    :params 列表，第一个参数为该视频的地址；第二个参数为其视频的排行榜分类
    """
    url = params[0]  # 视频地址
    time.sleep(0.5)

    res = requests.get(url)  # 请求视频地址
    response = res.text  # 获取文本
    html = etree.HTML(response)
    analysis_html(params, html)  # 调用解析文本的函数


async def async_get_detail(params):
    """
    异步函数，用来创建任务，并且开启事件循环
    :params 列表，第一个参数为该视频的地址；第二个参数为其视频的排行榜分类
    """
    global session, semaphore
    url = params[0]
    async with semaphore:
        async with session.get(url) as res:
            response = await res.text()
            await asyncio.sleep(0.5)
            html = etree.HTML(response)
            analysis_html(params, html)


def analysis_html(params, html):
    """
    解析html文本，获取需要的data,并且存储在对应的列表中
    :params 列表，第一个参数为该视频的地址；第二个参数为其视频的排行榜分类
    :html 需要解析的html文本
    """
    try:
        title = html.xpath('//*[@id="viewbox_report"]/h1/span/text()')[0].strip()  # 视频标题

        temp = html.xpath('//*[@id="member-container"]/div/div/a/text()')
        author = ''  # 视频作者(可能存在多人创作)
        if len(temp) != 0:
            for i in temp:
                author += i
                if temp.index(i) != (len(temp) - 1):
                    author += '&'
        else:
            author = html.xpath('//*[@id="v_upinfo"]/div[2]/div[1]/a[1]/text()')[0].strip()

        pubdate = html.xpath('//*[@id="viewbox_report"]/div/span[3]/text()')[0].strip()  # 发布时间

        temp = html.xpath('//*[@id="viewbox_report"]/div/span[1]/text()')[0].strip()
        play_volume = float(temp[0:-5])  # 播放量(万)，去除多余的汉字,转化为float类型

        barrage = html.xpath('//*[@id="viewbox_report"]/div/span[2]/text()')[0].strip()  # 弹幕数量

        temp1 = html.xpath('//*[@id="v_tag"]/ul/li/div/a/span/text()')
        temp2 = html.xpath('//*[@id="v_tag"]/ul/li/a/span/text()')
        temp3 = html.xpath('//*[@id="v_tag"]/ul/li/div/a/text()')
        classification = []  # 视频分类(多个分类，且每个分类下的标签格式不一样,同时需要去重,最后将其转化为字符串)
        for i in temp1:
            if i.strip() not in classification:
                classification.append(i.strip())
        for i in temp2:
            if i.strip() not in classification:
                classification.append(i.strip())
        for i in temp3:
            if i.strip() not in classification:
                classification.append(i.strip())
        classification = '&'.join(classification)

        likes = html.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]/text()')[0].strip()  # 点赞数

        coins = html.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[2]/text()')[0].strip()  # 投币数

        collect = html.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[3]/text()')[0].strip()  # 收藏数

        share = html.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[4]/text()')[0].strip()  # 转发数

        result = [title, author, pubdate, play_volume, barrage, classification, likes, coins, collect, share, params[0]]

        if params[1] == 'MUSIC':
            MUSIC.append(result)
        elif params[1] == 'DANCE':
            DANCE.append(result)
        elif params[1] == 'GAME':
            GAME.append(result)
        elif params[1] == 'KNOWLEDGE':
            KNOWLEDGE.append(result)
        elif params[1] == 'DIGITAL':
            DIGITAL.append(result)
        elif params[1] == 'CAR':
            CAR.append(result)
        elif params[1] == 'LIFE':
            LIFE.append(result)
        elif params[1] == 'FOOD':
            FOOD.append(result)
        elif params[1] == 'ZOO':
            ZOO.append(result)
        elif params[1] == 'ENTERTAINMENT':
            ENTERTAINMENT.append(result)
        else:
            MOVIES.append(result)
        logging.info(result)
    except:
        logging.error('{} failed.'.format(params[0]))


def save_data():
    """
    用来保存为csv文件,同时保存到数据库中
    """
    url = 'http://60.205.201.200/{}/'  # 目标地址
    headers1 = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    columns = ['title', 'author', 'pubdate', 'play_volume', 'barrage', 'classification', 'likes', 'coins', 'collect',
               'share', 'url']
    df = pd.DataFrame(MUSIC)
    df.columns = columns
    url1 = url.format('MUSIC')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/MUSIC.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(DANCE)
    df.columns = columns
    url1 = url.format('DANCE')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/DANCE.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(GAME)
    df.columns = columns
    url1 = url.format('GAME')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/GAME.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(KNOWLEDGE)
    df.columns = columns
    url1 = url.format('KNOWLEDGE')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/KNOWLEDGE.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(DIGITAL)
    df.columns = columns
    url1 = url.format('DIGITAL')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/DIGITAL.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(CAR)
    df.columns = columns
    url1 = url.format('CAR')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/CAR.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(LIFE)
    df.columns = columns
    url1 = url.format('LIFE')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/LIFE.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(FOOD)
    df.columns = columns
    url1 = url.format('FOOD')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/FOOD.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(ZOO)
    df.columns = columns
    url1 = url.format('ZOO')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/ZOO.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(ENTERTAINMENT)
    df.columns = columns
    url1 = url.format('ENTERTAINMENT')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/ENTERTAINMENT.csv', index=False, encoding='utf-8_sig')

    df = pd.DataFrame(MOVIES)
    df.columns = columns
    url1 = url.format('MOVIES')  # 构造不同的url
    data = df.to_json(orient='records')
    logging.info(requests.post(url1, data=data, headers=headers1))
    df.to_csv('results/MOVIES.csv', index=False, encoding='utf-8_sig')


async def async_func(urls):
    """
    创建异步函数任务，并且开始挂起，即爬取详细信息
    """
    global session
    tasks = [asyncio.ensure_future(async_get_detail(i)) for i in urls]
    await asyncio.gather(*tasks)
    await session.close()


def dispatch_task():
    """
    程序总的调度函数，安排各程序的执行逻辑
    """
    set_session()
    urls = get_all_urls()  # 先取得所有需要爬取的视频的url

    # start1 = time.time()
    # for i in urls:
    #     get_detail(i)
    # end1 = time.time()
    # save_data()

    logging.info('start async function.')
    start2 = time.time()
    asyncio.get_event_loop().run_until_complete(async_func(urls))  # 调用异步函数
    end2 = time.time()
    logging.info('end async function.')
    save_data()

    # logging.info('normal cost time {}s.'.format(end1 - start1))
    logging.info('async cost time {}s.'.format(end2 - start2))


if __name__ == '__main__':
    dispatch_task()
