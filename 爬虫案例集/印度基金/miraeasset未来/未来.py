#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :未来.py
# @Time     :2024/6/1814:59
# @Author   :aczhang
import execjs
import requests
import json

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.miraeassetmf.co.in",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "ASP.NET_SessionId": "kqyds43lwqdej02x4etz5tml",
    "_gcl_au": "1.1.550087535.1718692884",
    "__stp": "eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJmYWUzODQ3Zi01ZjFhLTRjYzgtODc3Yi03N2JjMTUzNGJjMTUifQ==",
    "_fbp": "fb.2.1718692888864.208040749353876080",
    "_ga": "GA1.3.1496647168.1718692889",
    "_gid": "GA1.3.890049001.1718692890",
    "__stgeo": "IjEi",
    "__stbpnenable": "MQ==",
    "__stdf": "MA==",
    "__stat": "ImZBeGc5enh6eEg4SDJ0U1BmLUNtVTc6QVBBOTFiRS1uTDRiYWlHaG5ObUY1eDFfS0EwZjBSODFiMm9POXdSSDRYVzc4NGxwWXpYQnd3bkxuZW5BRWxMN19rT1dXWE9QaXZtQnF3OURqY2hoSGRiVmgzUHVhUnBqVzJJQlg5NmFCZEIwZXVvVFpvTFBWY01mUXQ4TXJwMTNXM0xJSjVMOUMzNUwi",
    "_ga_3WG9TE7TEL": "GS1.1.1718692889.1.1.1718695208.60.0.0"
}
url = "https://www.miraeassetmf.co.in/AjaxService/GetDownloadsData"
js_code = execjs.compile(open("未来.js", encoding="utf-8").read())

request = {
    "modulename": "Factsheet",
    "pgno": 1,
    "pgsize": 10
}
# data = json.dumps(request, separators=(',', ':'))
request_data = js_code.call("EncryptFunction", request)
print(request_data)

# 不要tm把request和request_data 搞混淆了
data = {
    "request":
        request_data
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
