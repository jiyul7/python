# 연합뉴스 속보
import requests
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format
import bs4

class yeonhapNews:

    url = "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y"

    def getSoup(self, url):
        res = requests.get(url)
        return bs4.BeautifulSoup(res.text, "html.parser")

    def getBodyNews(self, url):
        url = "https://news.naver.com/main/list.nhn" + url
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        pagebodynews = []
        body = soup.find("ul", {"class":"type02"})
        list = body.findAll("li", {"class":"_rcount"})

        for li in list:
            row = li.find("span", {"class":"date"}).text.strip() + ": " + li.find("a").text.strip()
            pagebodynews.append(row)
        return pagebodynews

    def topNews(self):
        topnews = []
        soup = self.getSoup(self.url)
        ################# Top news
        tbody = soup.find("dl", {"class":"type04"})
        top = tbody.find("dt", {"class":""})
        topnews.append(top.text)
        # etc
        topEtc = tbody.findAll("li", {"class":"_rcount"})
        for one in topEtc:
            row = one.find("a").text
            topnews.append(row)
        return topnews

    def bodyNews(self, max):
        soup = self.getSoup(self.url)
        ################ Body news (get href + max page)
        limit = soup.find("div", {"class":"paging paging_ytn"})
        limit = limit.findAll("a")  # list안에 <a> </a>, 들만 쌓이면 find() 사용할 필요없이 바로 tag.text로 출력
        bodyNewsUrl = []
        page = 1
        for a in limit:
            if page > max:
                break
            bodyNewsUrl.append(a['href'])
            page = page + 1

        firstPage = bodyNewsUrl[0]
        firstPage = firstPage.replace("page=2", "page=1")
        bodyNewsUrl.insert(0,firstPage)

        ################ Body news
        allBodyNews = []

        for url in bodyNewsUrl:
            allBodyNews = allBodyNews + self.getBodyNews(url)

        allBodyNews.sort(reverse=True)
        return allBodyNews

# Robot = yeonhapNews()
# top = Robot.topNews()
# for i in top:
#     print(i)
# body = Robot.bodyNews()
# for j in body:
#     print(j)