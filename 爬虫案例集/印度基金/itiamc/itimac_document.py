#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :itimac_document.py
# @Time     :2024/6/1813:52
# @Author   :aczhang
import requests
import json
import execjs

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
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
url = "https://itiamc.com/jeeth/api/v1/catalog/getPartnerDocumentByType"

js_code=execjs.compile(open("itiamc.js", encoding="utf-8").read())

encrypt_data={
    "type": "Disclosure",
}
# dumps_data=json.dumps(encrypt_data, separators=(',', ':'))
# print(dumps_data)
eData=js_code.call("encryptData2","https://itiamc.com/jeeth/api/v1/catalog/getPartnerDocumentByType",encrypt_data)
print(eData.get("eData"))

data = {
    "eData": eData.get("eData")
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

res_data=js_code.call('decryptData',response.json().get("eData"))
print(res_data)
# print(response.text)
print(response)