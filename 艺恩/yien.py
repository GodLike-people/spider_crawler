#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :yien.py
# @Time     :2024/5/3114:26
# @Author   :aczhang
import execjs
import requests

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.endata.com.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'sdate': '2024-05-13',
    'MethodName': 'BoxOffice_GetWeekInfoData',
}

response = requests.post('https://www.endata.com.cn/API/GetData.ashx', headers=headers, data=data)

process_data=execjs.compile(open('yien_quan.js','r').read()).call("webInstace.shell",response.text)

print(process_data)