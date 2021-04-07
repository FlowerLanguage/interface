import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import logging
import random
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[Line：%(lineno)d] - %(levelname)s %(message)s',
                    filename='Logs/novel.txt',
                    filemode='a')
session = requests.Session()  # 创建一个全局Session对象


def is_existence_path(path):  # 判断文件价是否存在，不存在就创建
    if not os.path.exists(path):
        os.mkdir(path)


def construct_main_pages(main_page='https://www.wenku8.net/modules/article/toplist.php?sort=allvisit', start_page=1,
                         end_page=138):
    """
    根据传来的主页和页码数返回第一层构造的网页
    :param end_page: 网页截至页数

    :param start_page: 网页起止页数
    :param main_page: 网站主页
    :return: 返回一个包含构造的网页的列
    表
    """
    url_sum = []
    for page in range(start_page, end_page + 1):
        url_sum.append(main_page + '&page={}'.format(str(page)))
    return url_sum


def set_session():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    param = {
        'username': 'ReasonBetray',
        'password': 'liuping1235',
        'usecookie': '0',
        'action': 'login',
        'submit': ''
    }
    global session
    session.post('https://www.wenku8.net/login.php', headers=headers, data=param)  # 使用post登录后，保留当前会话，来获取数据


def get_novels_per_page(url):
    """
    根据网页，获取每个网页包含的小说数量
    :param url: 目标网页
    :return: 包含这个网页所有小说的列表
    """
    time.sleep(0.5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    global session
    try:
        novel_sum = []  # 用于存储小说详情页面的列表
        res = session.get(url, headers=headers)
        res = res.text.encode('ISO-8859-1').decode('gbk')
        html = BeautifulSoup(res, 'html.parser')
        table = html.find('table', class_='grid')  # 找到包含小说的table
        b_s = table.find_all('b')  # 进一步找到所有小说的b
        for b in b_s:
            href = b.a['href']  # 得到b标签下的a标签中的href属性
            novel_sum.append(href)  # 获得小说的详细连接，存入列表中
        print(novel_sum)
        return novel_sum
    except:
        logging.error('scrap {}   failed!'.format(url))


def get_novel_detail(novel_url):
    """
    根据传来的每个网页
    :param session: 利用session请求网页
    :param novel_url: 目标地址
    :return: 包含当前目标地址的小说的提取信息的字典
    """
    time.sleep(random.random())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    global session
    try:
        detail = dict()
        res = session.get(novel_url, headers=headers)
        try:
            res = res.text.encode('ISO-8859-1').decode('gbk')
        except:
            res = res.text.encode('ISO-8859-1').decode('gb18030')
        res = BeautifulSoup(res, 'html.parser')
        div = res.find(id='content')  # 找到第一个id为content的div标签
        div = div.find_all('div')[0]
        ntitle = div.find_all('tr')[0].find('b').text  # 找到b标签下面的小说标题
        content = div.find_all('tr')[2].find_all('td')  # 找到文库分类，小说作者，文章状态，最后更新，全文长度
        nclassification = content[0].text
        nclassification = nclassification.split('：')[1]  # 数据清洗，需要提取第二部分
        nauthor = content[1].text
        nauthor = nauthor.split('：')[1]
        nstatus = content[2].text
        nstatus = nstatus.split('：')[1]
        try:  # 有的小说并没有包含下面的全部信息，加容错，如果未找到，都设置为None
            nupdate = content[3].text
            nupdate = nupdate.split('：')[1]
            nlength = content[4].text
            nlength = int(float(nlength.split('：')[1][0:-1]))
        except:
            nupdate = None
            nlength = None

        ncover = div.find_all('tr')[3].find('img')['src']  # 获取到封面地址
        detail['小说名称'] = ntitle
        detail['文库分类'] = nclassification
        detail['小说作者'] = nauthor
        detail['文章状态'] = nstatus
        detail['最后更新'] = nupdate
        detail['全文长度'] = nlength
        detail['小说封面'] = ncover
        print(detail)
        logging.info('crawl {} success!'.format(novel_url))
        return detail
    except:
        logging.debug('need to crawl {} again!'.format(novel_url))
        return None


def post_data(path):
    """
    读取csv中的数据，先修改列名，再转换为json后发送
    """
    headers = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    url = 'http://60.205.201.200/hot_novel/'
    df = pd.read_csv(path)  # 读取数据
    df.columns = ['title', 'classification', 'author', 'status', 'update', 'length', 'cover']  # 更改列名

    temp = df['update'].isna()
    df.loc[temp, 'update'] = '2000-1-1'
    temp = df['length'].isna()
    df.loc[temp, 'length'] = 0

    data = df.to_json(orient='records')
    logging.info(str(sys.getsizeof(data) / 1024.) + 'kb！')
    res = requests.post(url, headers=headers, data=data)
    print(res)
    logging.info('post is {}'.format(res))


def dispatch_get_light_novel_library_solo():
    """
    获取轻小说文库内容的函数，安排调用关系，单
    采用先爬取所有详情页小说的网址，保存到novel_txt(每次爬取，需先创建)内，后续逐步读取，爬取，等循环完毕后，文件无内容，然后就执行发送数据；
    """
    set_session()  # 调用创建session对象的函数,获取
    path = os.getcwd() + '\\results\\'  # 结果保存文件路径以及文件名
    is_existence_path(path)  # 判断路径是否存在

    logging.info('start func Solo!')

    url_sum = construct_main_pages()  # 调用构造网页的函数，得到一个包含所有网页数的列表

    novel_sum = []  # 保存所有小说详情网页的列表
    txt = 'novel_url.txt'  # 用来保存提取的所有小说详情页的网址，就是将novel_sum中的内容存入novel_sum中
    csv = 'novel.csv'  # 用来保存提取的信息
    if os.path.exists(path + txt):  # 记录url的文件存在，即设定的开始爬取数据

        logging.info('start crawl!')
        with open(path + txt, 'r') as file:
            results = file.readlines()  # 读取文本中所有内容
        os.remove(path + txt)  # 删除文本
        if len(results) == 0:  # 文本中没有网址，即刚开始爬虫。需先获取网址;并创建csv文件

            logging.info('start crawl url!')
            for url in url_sum:  # 依次遍历所有主网页，获取所有主网页中包含的目标小说的网址，使用novel_sum列表保存
                if not novel_sum:
                    novel_sum = get_novels_per_page(url)
                else:
                    novels = get_novels_per_page(url)
                    for novel in novels:
                        novel_sum.append(novel)
            with open(path + txt, 'w') as file:  # 将爬取的小说详情页的网址写入txt文本中
                for i in novel_sum:
                    file.write(i + '\n')

            logging.info('end crawl url!')
            df = pd.DataFrame([{'小说名称': 1, '文库分类': 2, '小说作者': 3, '文章状态': 4, '最后更新': 5, '全文长度': 6, '小说封面': 7}])
            df = df.drop(labels=[0], axis=0)
            df.to_csv(path + 'novel.csv', encoding='utf-8_sig', index=False, mode='a')  # 即第一次运行爬虫文件时，需先创建一个csv文件
        else:  # 即文本中有网址，调用爬取数据的函数,如果返回None，则跳出循环

            logging.info('start crawl detail,url have {}.'.format(len(results)))
            novel_detail = []  # 保存所有小说的列表，每个列表元素是一个包含提取信息的字典
            over = True  # 用来判断txt中是否还有url，默认为True，即全部爬取完毕；否则设置为false即有错误.
            for i in results:
                origin = i
                i = i.strip()
                temp = get_novel_detail(i)  # 获取到小说的详细数据
                if temp is not None:  # 返回有数据，则保存
                    novel_detail.append(temp)
                    index = results.index(origin) + 1
                else:  # 返回None,记录该url的索引，并退出该循环
                    index = results.index(origin)
                    over = False
                    break
            df = pd.DataFrame(novel_detail)  # 将所有结果构造的列表保存为DataFrame对象
            df.to_csv(path + 'novel.csv', encoding='utf-8_sig', index=False, mode='a', header=False)  # 将爬取的数据添加到csv中
            if over:  # 全部提取完毕
                logging.info('所有url已爬取完毕!')
            else:  # 有未提取的url，将其结果保存到txt中
                with open(path + txt, 'w') as file:  # 将剩余未爬取的网址写入txt中
                    for i in results[index:]:
                        file.write(i.strip() + '\n')
            logging.info('remain url {}.'.format(len(results) - index))
            logging.info('end crawl,' + '  Novels have {number} '.format(number=len(novel_detail)))

    else:  # 记录url的文件不存在，存在两种情况。已经爬取了数据等待发送，发送完毕后需删除改文件;未爬取数据，即不开始改爬虫
        if os.path.exists(path + csv):
            print('发送数据')
            try:
                post_data(path + csv)
                over = True  # 用来判断是否成功发送,后面用来判断是否删除文件
            except:
                logging.error('发送数据错误!')
                over = False
            if over:
                os.remove(path + csv)
            else:
                pass

        else:
            print('什么都没做')
    logging.info('end func Solo!')


if __name__ == '__main__':
    dispatch_get_light_novel_library_solo()
