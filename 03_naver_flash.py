import urllib.request 
import bs4
 
# 경제속보 : 부동산 : 제목형

<<<<<<< HEAD
url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=260&sid1=101&mid=sec&listType=title&date=20200730&page=1"
=======
url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=260&sid1=101&mid=sec&listType=title&date=20200731&page=1"
>>>>>>> bdad0f55b5230eeb9b89ffeccf12423f226a15d1

html = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(html, "html.parser")

flash_body = soup.find("div", {"class":"list_body newsflash_body"})

allul = flash_body.findAll("ul")

for ul in allul:
    allli = ul.findAll("li")
    for li in allli:
        # 신문사
        # 내용
        print(li.find("span", {"class":"writing"}).text.strip() +
             ":" + li.find("a").text.strip())
        print
        # print(li.find("span", {"class":"date is_new"}).text)
