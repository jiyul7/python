# url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=260&sid1=101&mid=sec&listType=title&date=20200731&page=1"

import requests
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format
import xml.etree.ElementTree as ET

url = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
post = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>#BZNO#</txprDscmNo><dongCode>82</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map><nts<nts>nts>20DrRf8wh0jC7XgmQs3RhHzMAEP3VhUf3MYsLX1snYGuE09"
try:
    headers = {'User-Agent': 'Mozilla/5.0','Connection': 'keep-alive'}
    # User-Agent값이 꼭 있어야 307에러 안 남

    #cj = requests.cookies.RequestsCookieJar()    
    # Cookie 세팅하려면 jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

    #res = requests.get(url, headers=headers, cookies=cj)
    # 전달값 : payload = {'key1':'value',,'key3':['value2', 'value3']} 
    # GET방식 : params=payload
    # POST방식 : data=payload
    kodit = "1058206004"
    for i in range(1):
        res = requests.post(url, headers=headers, data=post.replace("#BZNO#", kodit))
    # data = res.json()
        pprint(res.text)
        output = ET.fromstring(res.text).findtext("trtCntn")
        
        print(output)
        res.close()

except HTTPError as inst:
    output = format(inst)
    print(output)