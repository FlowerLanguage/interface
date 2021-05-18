import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import logging
import pandas as pd
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filemode='a',
                    filename='Logs/book.txt')

CURRENCY = 4  # 设置最大并发量
semaphore = asyncio.Semaphore(CURRENCY)  # 创建信号量
session = None  # 创建session对象
df = []  # 用来存储提取的book


def construct_main_page(start_page=1, end_page=50):
    """
    根据end_page构造主网页数目
    :return urls包含所有构造的网页数
    """
    logging.info('construct main page.')
    urls = []
    for i in range(start_page, end_page):
        url = 'https://www.dushu.com/book/1175_{}.html'.format(i)
        urls.append(url)
    return urls


def get_book_url(main_urls):
    """
    根据参数main_urls提取当页包含的所有book的链接,由于传入了所有主网页，因此此函数会将所有主网页提取完后返回所有book链接
    :main_urls 构造的所有主网页
    """
    logging.info('start get all book url.')
    urls = []  # 用来存储提取的所有book链接
    for i in main_urls:
        res = requests.get(i)
        res = BeautifulSoup(res.text, 'html.parser')
        book_list = res.find(class_='bookslist')  # 所有的小说在bookslist类下面
        lis = book_list.find_all('li')  # 每本book就是一个li，一个主网页包含40本book
        for li in lis:
            a = li.find('a')
            basic_url = 'https://www.dushu.com' + a['href']  # 构造book链接
            urls.append(basic_url)
    logging.info('end get all book urls.')
    return urls


async def get_book_detail(book_url):
    """
    提取每本book的细节，包括书本名，封面，作者，出版社，ISBN，出版时间，包装，详细地址
    """
    logging.info('crawl {}.'.format(book_url))
    global session
    global df
    async with semaphore:
        async with session.get(book_url) as res:
            text = await res.text()
            res = BeautifulSoup(text, 'html.parser')
            detail = res.find(class_='bookdetails-left')
            book_title = detail.find('h1').text  # 书本名
            book_cover = detail.find('img')['src']  # 封面
            tds = detail.find_all('td')  # 需要提取的信息都在td中，先找到所有的td再对应
            book_author = tds[1].text  # 作者
            book_publisher = tds[3].text  # 出版社
            book_ISBN = tds[9].text  # ISBN
            book_time = tds[11].text  # 出版时间
            book_pack = tds[13].text  # 包装
            if book_pack == '':
                book_pack = '未确定'
            result = [book_title, book_cover, book_author, book_publisher, book_ISBN, book_time, book_pack, book_url]
            df.append(result)


async def async_task(urls_book):
    """
    异步的调度函数，创建异步任务，挂起
    """
    logging.info('start async function.')
    global session
    session = aiohttp.ClientSession()
    tasks = [asyncio.ensure_future(get_book_detail(i)) for i in urls_book]
    await asyncio.gather(*tasks)
    await session.close()
    logging.info('end async function.')


def post_data():
    """
    调用全局变量发送数据到服务器
    """
    logging.info('start post data.')
    headers = {
        'Authorization': 'Token 9345eca2ef271fd25dcec1b6e5f6ab3759836c09',
        'Content-Type': 'application/json'
    }
    url = 'http://60.205.201.200/book/'
    global df
    df = pd.DataFrame(df)
    df.columns = ['title', 'cover', 'author', 'publisher', 'isbn', 'time', 'pack', 'url']
    print(df.describe())
    logging.info('post data {}kb!'.format(sys.getsizeof(df) / 1024.))
    data = df.to_json(orient='records')
    print(requests.post(url, data=data, headers=headers))  # 发送data数据给服务器
    logging.info('end post data')


def dispatch_task():
    """
    总调度函数
    """
    logging.info('Start Progress!')
    urls_page = construct_main_page()
    urls_book = get_book_url(urls_page)
    asyncio.get_event_loop().run_until_complete(async_task(urls_book))  # 调用异步函数
    post_data()
    logging.info('End Progress!')


if __name__ == '__main__':
    dispatch_task()
