import os

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# 设置浏览器窗口的位置和大小
browser.set_window_position(0, 0)
browser.set_window_size(1000, 700)
wait = WebDriverWait(browser, 10)

basedir = "jiandan"


def get_page_num(url):
    '''
    :param url:  要请求的煎蛋网的url
    :return:  返回当前请求的url的html内容
    '''
    print("正在爬取{}...".format(url))
    try:
        browser.get(url)
        html = browser.page_source
        if html:
            pares_one(html)
    except EOFError:
        print("网页不存在")
        return None


def pares_one(html):
    soup = BeautifulSoup(html, 'lxml')
    currentPage = soup.select('#body #comments  .comments .cp-pagenavi span')[1].text.strip()[1:-1]  # 当前页数
    nextPage = int(currentPage) - 1
    # 创建文件夹
    pageDir = basedir + "/" + currentPage
    if not os.path.exists(pageDir):
        os.makedirs(pageDir)
    pics = soup.find_all("a", class_="view_img_link")
    for i in range(len(pics)):
        picUrl = pics[i]['href']
        download_img(pageDir, picUrl)

    if nextPage != 0:
        html = "http://jandan.net/ooxx/page-{}#comments".format(nextPage)
        get_page_num(html)
    else:
        print("已经爬取了所有的图片资源")


def download_img(pageDir, url):
    '''
    下载当前页面下所有的妹子图片
    :param pageDir:
    :param url:
    :return:
    '''
    index = str(url).rfind("/")  # 找到最后 / 位置
    fileName = url[index:]
    filePath = pageDir + fileName
    url = "http:" + url
    response = requests.get(url)
    source = response.content  # 获取图片的二进制数据
    with open(filePath, "wb") as f:
        f.write(source)
        f.close()
        response.close()
        print("{}图片保存成功".format(filePath))


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    get_page_num(url)
