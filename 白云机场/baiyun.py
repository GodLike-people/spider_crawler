#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :baiyun.py
# @Time     :2024/5/2713:06
# @Author   :aczhang
import execjs
import requests
import json

json_data = {
    'type': '1',
    'terminal': '',
    'day': 0,
    'depOrArr': '1',
    'pageNum': 2,
    'pageSize': 15,
}
json_data_dumps = json.dumps(json_data)
data=execjs.compile(open("baiyun.js",'r',encoding='utf-8').read()).call("get_data",json_data_dumps)
print(data)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'Hm_lpvt_0effb2f651854e064f7d24a159e08bd5=1716786359; Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a=1716786359; Hm_lpvt_483eff6efca2ca9bff48af354895a36f=1716786359; Hm_lpvt_783519365e6df848bd882229527a15bc=1716786359; Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1716786359; Hm_lvt_0effb2f651854e064f7d24a159e08bd5=1716786359; Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a=1716786359; Hm_lvt_483eff6efca2ca9bff48af354895a36f=1716786359; Hm_lvt_783519365e6df848bd882229527a15bc=1716786359; Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1716786359; JSESSIONID=tPF-Mq6UfTqT8rOxo22djfNQ8qPEhH0NQsxuOmBn; Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1716786359; Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1716786359; Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a=1716786359; Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a=1716786359; Hm_lvt_783519365e6df848bd882229527a15bc=1716786359; Hm_lpvt_783519365e6df848bd882229527a15bc=1716786359; Hm_lvt_0effb2f651854e064f7d24a159e08bd5=1716786359; Hm_lpvt_0effb2f651854e064f7d24a159e08bd5=1716786359; Hm_lvt_483eff6efca2ca9bff48af354895a36f=1716786359; Hm_lpvt_483eff6efca2ca9bff48af354895a36f=1716786359; JSESSIONID=P-PphP7cu4HU-Md0A-v5atJdFOUsVtLKDkvat5v4',

    'Origin': 'https://www.baiyunairport.com',
    'Referer': 'https://www.baiyunairport.com/flight/dep',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',

    'Signature': data[0],
    'Timestamp': str(data[1]),
    'Nonce': data[2],

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'locale': 'zh_CN',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
print(headers)

response = requests.post(
    'https://www.baiyunairport.com/byairport-flight/flight/list',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)