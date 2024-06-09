import json

import execjs
import requests

cookies = {
    # 'W_CITY_S_V': '120',
    # 'R_SCH_CY_V': '5685330',
    # 'wd_guid': 'af711ad8-b32b-47dd-8c1c-e67e2648f14f',
    # 'historyState': 'state',
    # '__c': '1717312330',
    # '__g': '-',
    # '__l': 'l=%2Fwww.kanzhun.com%2F&r=',
    # 'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1715864252,1715906404,1717312332',
    # '__a': '45315421.1715864246.1715906404.1717312330.16.3.3.16',
    # 'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1717312455',
    # 'wbrwsid': '43234552',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'W_CITY_S_V=120; R_SCH_CY_V=5685330; wd_guid=af711ad8-b32b-47dd-8c1c-e67e2648f14f; historyState=state; __c=1717312330; __g=-; __l=l=%2Fwww.kanzhun.com%2F&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1715864252,1715906404,1717312332; __a=45315421.1715864246.1715906404.1717312330.16.3.3.16; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1717312455; wbrwsid=43234552',
    'href': 'https://www.kanzhun.com/search?cityCode=101010100&industryCodes=&pageNum=1&query=%E7%88%AC%E8%99%AB&type=1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kanzhun.com/search?cityCode=101010100&industryCodes=&pageNum=1&query=%E7%88%AC%E8%99%AB&type=1',
    'reqsource': 'fe',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    # 'traceid': '62606ead-0912-4e19-ad9c-9b37072ed838',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
# data2 = '{"query":"爬虫","pageNum":1,"limit":15}'
data2 = {
    "query": "爬虫",
    "pageNum": 1,
    "limit": 15
}

js_code=execjs.compile(open("kanzhun.js",encoding='utf8').read())
data=js_code.call("get_params",json.dumps(data2,separators=(',', ':')))
print(data)
print(data2)
# print(json.dumps(data,separators=(',', ':')))
# data={
#   'kiv': 'C8BtQE5wGm86KpEw',
#   'b': 'U4qZZNy4lUTxf7LzFHrdL5wMMXzPh4GgocZbJkAEYyJ8dNN07cHjSEsKHO9mokQH'
# }

# data={
#   'getTraceID': 'fdc745e4-66ad-4465-87f6-a1a697f7daf7',
#   'b': '_sD-CLaEriTmKPxgCC7MZBjUQVZKwwlUYjHwxqod89FXTUxHu-gXXnMEmM7qqunl',
#   'kiv': 'C8BtQE5wGm86KpEw'
# }
# headers['traceid']=data['getTraceID']
params = {
    'b': data['b'],
    'kiv': data['kiv'],
}
print(params)
# print(headers)
response = requests.get('https://www.kanzhun.com/api_to/search/company_v2.json', params=params, cookies=cookies, headers=headers)
# print(response.text)
data3=js_code.call("c" ,response.text,data['kiv'])
print(data3)
