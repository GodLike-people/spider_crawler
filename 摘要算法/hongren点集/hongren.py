import execjs
import requests
import json
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.hh1024.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'param': '{"no":"dy3009","data":{}}',
    # 'sign': '9d19abacffe0b16f5c0569ac588cbab58418a8f82d034e92dcab2865cea38420',
    # 'timestamp': 1716994698939,
    'tenant': '1',
    'token': 'h622inzcXnQ1vzRaB58045Zk6GQ69UDP',
}
param=json.dumps(json_data.get("param"))
# param=json_data.get("param")
print(param)
get_params=execjs.compile(open('hongren.js','r',encoding='utf-8').read()).call("get_params",param)
json_data['timestamp']=get_params[0]
json_data['sign']=get_params[1]
print(json_data)

response = requests.post('https://ucp.hrdjyun.com:60359/api/dy', headers=headers, json=json_data)
print(response.text)