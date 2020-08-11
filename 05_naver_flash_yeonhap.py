# 연합뉴스 속보
import requests
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format
import bs4

# url = "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=20200806&page=1" 
url = "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y"

res = requests.get(url)
# print(res.text)
soup = bs4.BeautifulSoup(res.text, "html.parser")

################# Top news
topnews = []
tbody = soup.find("dl", {"class":"type04"})
top = tbody.find("dt", {"class":""})
topnews.append(top.text)
# etc
topEtc = tbody.findAll("li", {"class":"_rcount"})
for one in topEtc:
    row = one.find("a").text
    topnews.append(row)
for a in topnews:
    print(a)

################ Body news (get max page)
limit = soup.find("div", {"class":"paging paging_ytn"})
limit = limit.findAll("a")  # list안에 <a> </a>, 들만 쌓이면 find() 사용할 필요없이 바로 tag.text로 출력
for b in limit:
    # print(b.text)
    max = b.text
print("MAX Page: " + max)

################ Body news
bodynews = []
body = soup.find("ul", {"class":"type02"})
list = body.findAll("li", {"class":"_rcount"})

for li in list:
    row = li.find("span", {"class":"date"}).text.strip() + ": " + li.find("a").text.strip()
    bodynews.append(row)

bodynews.sort(reverse=True)
for a in bodynews:
    print(a)


