#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :itimac_Nav.py
# @Time     :2024/6/1813:28
# @Author   :aczhang
import execjs
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
    "Connection": "keep-alive",
    "Origin": "https://www.itiamc.com",
    "Referer": "https://www.itiamc.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://itiamc.com/jeeth/api/v1/catalog/getLatestNav"
response = requests.get(url, headers=headers)

# print(response.text)

data=execjs.compile(open("itiamc.js", encoding="utf-8").read()).call('decryptData', response.json().get("eData"))
print(data)