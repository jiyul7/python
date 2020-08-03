
# from urllib.request import build_opener, HTTPCookieProcessor
# opener = build_opener(HTTPCookieProcessor())
# response = opener.open("https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000")
# print(response.read())

# You need a http.cookiejar.CookieJar and a urllib.request.HTTPCookieProcessor to avoid the redirect loop:
# https://stackoverflow.com/questions/32569934/urlopen-returning-redirect-error-for-valid-links

# from 모듈(namespace) import 함수(in 모듈) as 별칭
# --> or 모듈.함수()

from urllib import request
# from html import parser
import requests

from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar
# from bs4 import BeautifulSoup
import json
from pprint import pprint   # json data pretty format

url = "https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000"   # mycortarNo는 로그인 후 사용하는 듯
try:
    # req=urllib.request.Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
    # User-Agent값이 꼭 있어야 307에러 안 남
    req=request.Request(url, None, {'User-Agent': 'Mozilla/5.0','Connection': 'keep-alive'})
    cj = CookieJar()

    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    res = opener.open(req)
    raw_res = res.read().decode('utf8', errors='ignore')

    data = json.loads(raw_res)
    # pprint(data)
    aaa = data.get("result").get("list")
    # pprint(aaa)
    for h in aaa:
        print(h.get("CortarNm"))
        
    # pprint(data)
    res.close()

except HTTPError as inst:
    output = format(inst)
    print(output)