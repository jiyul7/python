# 경제속보 : 부동산 : 제목형
# url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=260&sid1=101&mid=sec&listType=title&date=20200731&page=1"

import requests
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format

url = "https://m.land.naver.com/map/getRegionList?cortarNo=0000000000&mycortarNo=0000000000"   # mycortarNo는 로그인 후 사용하는 듯
try:
    headers = {'User-Agent': 'Mozilla/5.0','Connection': 'keep-alive'}
    # User-Agent값이 꼭 있어야 307에러 안 남

    cj = requests.cookies.RequestsCookieJar()    
    # Cookie 세팅하려면 jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

    res = requests.get(url, headers=headers, cookies=cj)
    # 전달값 : payload = {'key1':'value',,'key3':['value2', 'value3']} 
    # GET방식 : params=payload
    # POST방식 : data=payload
    
    data = res.json()
    # pprint(data)
    lists = data.get("result").get("list")
    for onerow in lists:
        print(onerow.get("CortarNm"))
        
    # pprint(data)
    res.close()

except HTTPError as inst:
    output = format(inst)
    print(output)