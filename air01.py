# 인터파크 항공권 조회
import requests
#from urllib import request
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

url = "https://domair.interpark.com/dom/main.do?trip=OW&dep=TAE&arr=CJU&dep2=CJU&arr2=TAE&depdate=20211231&retdate=20220102&adt=1&chd=0&inf=0&mbn=tourair&mln=airdome_search1#anchor-list"

res = requests.get(url)
soup = BeautifulSoup(res.text, features="html.parser")

#pprint(soup)

list = soup.select('li.txt-type1')
pprint(list)

#topnews.append(top.text)
# etc
#topEtc = tbody.findAll("li", {"class":"_rcount"})
#for one in list:
 #   row = one.text
    #print(row)
