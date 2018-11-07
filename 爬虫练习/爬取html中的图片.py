import os
import time
import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# 本次爬取的是html网页中带有图片地址的，简单网站

def getPicCategory(url):
    ua = UserAgent()
    root = "D:/pythonpic/"
    response = requests.get(url, headers={"User-Agent": ua.random})
    response.close()
    if response.status_code == 200:
        source = response.text
        soup = BeautifulSoup(source, 'html.parser')
        pics = soup.find_all("div", class_="syl_info")

        if len(pics) == 0:
            print("没有要爬取的图片资源")
            return

        # 创建文件夹
        for i in range(len(pics)):
            dir_name = pics[i].find('a').text.strip()
            dir_path = root + dir_name
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            pics_url = url + pics[i].find('a')["href"]
            print("{}文件夹创建完毕".format(dir_path))
            getCategoryPics(dir_path, url, pics_url)
    else:
        print("网络请求失败{}".format(url))


def getCategoryPics(dir_path, baseurl, url):
    response = requests.get(url)
    response.close()
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    pics = soup.find_all("div", class_="il_img")
    if len(pics) == 0:
        print("没有任何数据可爬取")
        return
    else:
        for pic in pics:
            item_url = baseurl + pic.find('a')['href']
            print("爬取{}图片".format(item_url))
            downloadUrl(dir_path, item_url)


def downloadUrl(dir_path, url):
    response = requests.get(url)
    response.close()
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    pic = soup.find("div", id="pic_con")
    file_name = soup.find('div', class_="al_tit").find('h1').text.replace(" ","")
    print(file_name)
    if pic:
        download_url = pic.find('img')['src']
        r = requests.get(download_url)

        file_path = dir_path +"/"+ file_name + ".jpg"
        with open(file_path, "wb")  as f:
            f.write(r.content)
            f.close()
            r.close()
            print("{}图片保存成功".format(file_path))
    else:
        print("不存在")


if __name__ == '__main__':
    url = "http://www.ivsky.com"
    getPicCategory(url)
