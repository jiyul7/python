import requests
 
# GET
resp = requests.get('http://httpbin.org/get')
print(resp.text)
 
# POST
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)

