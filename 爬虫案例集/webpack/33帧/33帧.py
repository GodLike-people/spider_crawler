import json

import execjs
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Origin": "https://fse.agilestudio.cn",
    "Referer": "https://fse.agilestudio.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "X-Signature": "",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://fse-api.agilestudio.cn/api/search?"
params = {
    "keyword": "风吹草",
    "page": "2",
    "limit": "12",
    "_platform": "web",
    "_versioin": "0.2.5",
    "_ts": "1718550826381"
}
params2=json.dumps(params,separators=(",",":"))
# print(params2)
data_dic=execjs.compile(open("33帧.js",encoding="utf-8").read()).call('d',params)
_ts=data_dic["time"]
data=data_dic["sign"]
print(data_dic)
headers["X-Signature"]=data
params["_ts"]=_ts
print(params)
print(headers["X-Signature"])
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)