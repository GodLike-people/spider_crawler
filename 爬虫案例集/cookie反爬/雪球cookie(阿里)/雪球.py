import re

import execjs
import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https://xueqiu.com/today",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

cookies = {
    "acw_tc": "",
    "acw_sc__v2": ""
}
url = "https://xueqiu.com/today"

session=requests.session()
res=session.get(url, headers=headers)
# print(res.cookies["acw_tc"])
cookies['acw_tc']=res.cookies["acw_tc"]
arg1 = re.search("var arg1='(.*?)';", res.text).group(1)
params = execjs.compile(open('雪球.js', encoding='utf-8').read()).call("get_cookie", arg1)
cookies['acw_sc__v2']=params
print(cookies)

response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
# print(response)