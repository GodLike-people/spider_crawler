#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :qimai.py
# @Time     :2024/5/2710:32
# @Author   :aczhang
import execjs
import requests

cookies = {
    'gr_user_id': 'b3c05395-6b28-49c2-8ec5-6e4ca6106cbe',
    'PHPSESSID': '9crn1oq0uiu5hha95rs93l7hfr',
    'qm_check': 'A1sdRUIQChtxen8pI0dAOTQ+GRdzfX0QZlkBAwgGUC03HBdkVV5RFABFIRUJCBETVkQSGAlIBAhVVlZdPEFTFXNbQlxTQAshV1ZIDgolAGgCEElDaw06VktIPEo+BAYbEhUSV1AABQxKQltKGQceABUAGAhHGw%3D%3D',
    'ada35577182650f1_gr_session_id': '746ace5c-800c-41d9-a096-8be37ddb3c8f',
    'synct': '1716777071.567',
    'syncd': '-1596',
    'tgw_l7_route': 'd09474674af82c17375cfcdd775c0c28',
    'ada35577182650f1_gr_session_id_sent_vst': '746ace5c-800c-41d9-a096-8be37ddb3c8f',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'gr_user_id=b3c05395-6b28-49c2-8ec5-6e4ca6106cbe; PHPSESSID=9crn1oq0uiu5hha95rs93l7hfr; qm_check=A1sdRUIQChtxen8pI0dAOTQ+GRdzfX0QZlkBAwgGUC03HBdkVV5RFABFIRUJCBETVkQSGAlIBAhVVlZdPEFTFXNbQlxTQAshV1ZIDgolAGgCEElDaw06VktIPEo+BAYbEhUSV1AABQxKQltKGQceABUAGAhHGw%3D%3D; ada35577182650f1_gr_session_id=746ace5c-800c-41d9-a096-8be37ddb3c8f; synct=1716777071.567; syncd=-1596; tgw_l7_route=d09474674af82c17375cfcdd775c0c28; ada35577182650f1_gr_session_id_sent_vst=746ace5c-800c-41d9-a096-8be37ddb3c8f',
    'origin': 'https://www.qimai.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
params = {
    'setting': '0',
    'genre': '5000',
}
value=params.values()
analysis=execjs.compile(open('qimai.js','r').read()).call("get_analysis",list(value))
params['analysis']=analysis
print(params)

response = requests.get('https://api.qimai.cn/indexV2/getIndexRank', params=params, cookies=cookies, headers=headers)
print(response.text)
print(response.json())
