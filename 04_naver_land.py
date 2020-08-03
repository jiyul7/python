import urllib.request
import bs4

def getsoup(url):
    html = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    print(soup)
    return soup

# 네이버 모바일 land 지역 목록 추출
 url01 = "https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000"
#  url01 = "https://m.land.naver.com/map?showon=select&isAdd=Y"
# url01 ="https://m.land.naver.com/map/37.496437:127.077115:18/APT:JGC/A1:B1:B2#regionStep1"
soup01 = getsoup(url01)
region01 = soup01.find("table", {"class":"region_table"})
region02 = region01.findAll("tr", {"class:":"region_row"})

print(region02)



