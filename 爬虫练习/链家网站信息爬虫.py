import requests
from fake_useragent import UserAgent  # 模拟请求头中UserAgent参数
import pandas as pd
from bs4 import BeautifulSoup  # 解析返回的html


class LianjiaSpider(object):
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.datas = list()

    # 查找符合条件的pageNum
    def getMaxPage(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')
            divs = soup.find_all('div', class_='page-box house-lst-page-box')
            max_page = None
            if len(divs) == 0:
                print("没有符合条件的数据：{}".format(url))
                return max_page
            else:
                max_page = eval(divs[0].attrs["page-data"])["totalPage"]
            return max_page
        else:
            print("请求失败 statue: {}".format(response.status_code))
            return None

    def parsePage(self, url):
        max_page = self.getMaxPage(url)
        if max_page is not None:
            for i in range(1, max_page + 1):
                page_url = (url + "pg{}/").format(i)
                print("当前正在爬取第{}页租房信息：{}".format(i, page_url))
                response = requests.get(page_url, headers=self.headers)
                if response.status_code == 200:
                    source = response.text
                    soup = BeautifulSoup(source, 'html.parser')
                    a = soup.find_all("div", class_="pic-panel")
                    for j in range(len(a)):
                        link = a[j].find('a')["href"]
                        print("第{}条租房信息 url :{}".format(j + 1, link))
                        detail = self.parsePageDetail(link)
                        self.datas.append(detail)
                else:
                    print("获取第{}页失败{}".format(i, url))
                print("所有数据爬取完毕，正在存储到csv文件中")
                data = pd.DataFrame(self.datas)
                data.to_csv("链家网租房数据.csv", encoding='utf_8_sig')

    def parsePageDetail(self, url):
        detail = {}
        response = requests.get(url)
        source = response.text
        soup = BeautifulSoup(source, 'html.parser')
        div = soup.find("div", class_="content zf-content")
        detail["月租金"] = float(div.find("span", class_="total").text.strip())
        detail["面积"] = div.find_all("p", class_="lf")[0].text[3:].strip()
        detail["房屋户型"] = div.find_all("p", class_="lf")[1].text[5:].strip()
        detail["楼层"] = div.find_all("p", class_="lf")[2].text[3:].strip()
        detail["房屋朝向"] = div.find_all("p", class_="lf")[3].text[5:].strip()
        detail["地铁"] = div.find_all("p")[4].text[3:].strip()
        detail["小区"] = div.find_all("p")[5].text[3:].split('-')[0].strip()
        detail["位置"] = div.find_all("p")[6].text[3:].strip()
        return detail


if __name__ == '__main__':
    url = url = "https://bj.lianjia.com/zufang/haidian/"
    spider = LianjiaSpider()
    spider.parsePage(url)
