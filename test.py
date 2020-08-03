
# from urllib.request import build_opener, HTTPCookieProcessor
# opener = build_opener(HTTPCookieProcessor())
# response = opener.open("https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000")
# print(response.read())

# You need a http.cookiejar.CookieJar and a urllib.request.HTTPCookieProcessor to avoid the redirect loop:
# https://stackoverflow.com/questions/32569934/urlopen-returning-redirect-error-for-valid-links
import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar
# from bs4 import BeautifulSoup
import json
from pprint import pprint   # json data pretty format

url = "https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000"   # mycortarNo는 로그인 후 사용하는 듯
try:
    req=urllib.request.Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(req)
    raw_response = response.read().decode('utf8', errors='ignore')
    data = json.loads(raw_response)
    # pprint(data)
    aaa = data.get("result").get("list")
    # pprint(aaa)
    for h in aaa:
        print(h.get("CortarNm"))
        
    # pprint(data)

    response.close()
except urllib.request.HTTPError as inst:
    output = format(inst)
    print(output)