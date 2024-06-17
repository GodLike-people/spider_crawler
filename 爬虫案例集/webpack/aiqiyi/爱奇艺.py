#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :爱奇艺.py
# @Time     :2024/6/1711:14
# @Author   :aczhang
import execjs
import requests


headers = {
    "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Referer": "https://www.iqiyi.com/",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://passport.iqiyi.com/apis/reglogin/login.action"
js_code=execjs.compile(open("爱奇艺.js", encoding="utf-8").read())
passwd="zac123456"
passwd2=js_code.call("rsaEnc",passwd)
print(passwd2)
params = {
    "__NEW": "1",
    "agenttype": "1",
    "app_version": "12.62.16353",
    "area_code": "86",
    "checkExist": "1",
    "device_id": "237d3307c43bddc26a23b15ad7eff508",
    "dfp": "",
    "email": "18952597616",
    "fromSDK": "1",
    "lang": "",
    "nr": "3",
    "passwd": passwd2,
    "ptid": "01010021010000000000",
    "sdk_version": "1.0.0",
    "verifyPhone": "1",
    "qd_sf": "36B4FA6A7B540D8A794A29DDA3762DB6_5_0_1718593944"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)