# from ntpath import join
import requests
from requests.exceptions import HTTPError
from pprint import pprint   # json data pretty format
import json
import time

def hometax_status(payload, outfd):
    
    url = "https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=fQt2dRi7TZxBFIMypcLbpssMXYLmKJPcr5kkgrX4jDQrynLz9SwRKURgJdn8H%2BHUTpLi9pXjZYkQNtZuWQXrhw%3D%3D"

    try:
        headers = {'User-Agent': 'Mozilla/5.0','Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8'}
        # User-Agent값이 꼭 있어야 307에러 안 남

        # payload = {'b_no':['1058206004', '5873900147']} 
        
        res = requests.post(url, headers=headers, json=payload)
            
        resdata = res.json()
        # pprint(resdata)
        
        # js4 = '{"id": 1, "info": [{"name": "helloalpaca", "email": "jms393497@gmail.com"}, {"name": "choppermask", "email": "abcde@abcde.com"}]}'
        # jsonObject = json.loads(js4) 
        # jsonArray  = jsonObject.get("info")
        
        jsonArray  = resdata.get("data")
        
        for list in jsonArray:
            # print("b_no: ", list.get("b_no"))
            # print("b_stt: ", list.get("b_stt"))
            # print("tax_type: ", list.get("tax_type"))
            outRow = list.get("b_no") + "|" + list.get("b_stt") + "|" + list.get("tax_type") + "\n"
            outfd.write(outRow)
        # pprint(data)
        res.close()
        # time.sleep(3)

    except HTTPError as inst:
        output = format(inst)
        print(output)
        print(outRow)
    # finally:
    #     print("nts end")
        
# input file 읽어서 json형태로 만들기
infd  = open("C:/git/python/hometax/file/input_bzno.txt", "r")
outfd = open("C:/git/python/hometax/file/output_bzno.txt", "w", encoding="utf-8")
# inputValue1 = fd.readlines()

# list를 만들고, dictionary로 만들기 : {'b_no':['1058206004', '5873900147']} 
li = []
cnt = 0
totalCnt = 0
payload = {}

for onerow in infd:
    if not onerow: break
    li.append(onerow.rstrip())
    cnt += 1
    totalCnt += 1
    
    if cnt % 100 == 0 and cnt > 1:
        payload = {'b_no':li}
        print(cnt)
        hometax_status(payload, outfd)
        print("%d Processed.." %totalCnt)
        cnt = 0
        li = []
        payload = {}
    
if cnt > 0:
    payload = {'b_no':li}
    hometax_status(payload, outfd)
    # print(cnt)
    print("%d Processed.."  %totalCnt)
    
infd.close()
outfd.close()
print("# JOB END: ", totalCnt)

