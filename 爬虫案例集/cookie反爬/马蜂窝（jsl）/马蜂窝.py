import re

import execjs
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https://www.mafengwo.cn/i/5376978.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.mafengwo.cn/i/5376978.html"
res = requests.get(url, headers=headers)
cookies = {
    "__jsluid_s": '',
    "__jsl_clearance_s": ""
}
# 生成的cookie __jsl_clearance_s
# print(res.text)
# 第一次请求返回的cookie参数
cookies["__jsluid_s"] = res.cookies["__jsluid_s"]
arg1 = re.search("<script>document.cookie=(.*?);location", res.text).group(1)
param=execjs.eval(arg1)
cookies["__jsl_clearance_s"]=param.split('ance_s=')[-1]
print(cookies)

# 第二次 带着生成的cookie和请求返回的参数，再法一次请求
res = requests.get(url, headers=headers,cookies=cookies)
print(res.text)
# 第三次根据第二次返回的js代码重新生成__jsl_clearance_s
