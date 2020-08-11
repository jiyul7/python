import urllib.request
import json
from pprint import pprint

url = "https://m.land.naver.com/map/getRegionList"

values = {
    "cortarNo": "0000000000",
    "mycortarNo": "0000000000"
}


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = json.dumps(values).encode("utf-8")
pprint(data)

try:
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
    pprint(res.decode())
except Exception as e:
    pprint(e)