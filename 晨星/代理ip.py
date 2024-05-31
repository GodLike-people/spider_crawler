#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :代理ip.py
# @Time     :2024/5/912:10
# @Author   :aczhang
from queue import Queue

import requests
import json

url = "http://www.baidu.com/"

header={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',

}

# 获取一个新的ip
def get_ip_queue():
    url3 = f'http://http.tiqu.alibabaapi.com/getip3?num=1&type=2&pack=129761&port=1&lb=1&pb=45&gm=4&regions='
    res3 = requests.get(url3)
    print(res3.text)
    ip = json.loads(res3.text)['data']
    # ip="59.60.121.185:4315"
    print(ip)
    # proxyHost = ip["ip"]
    # proxyPort = ip["port"]
    proxyHost = "59.60.121.185"
    proxyPort = "4315"

    proxyHttp = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }
    # proxyHttps = "https://%(host)s:%(port)s" % {
    #     "host": proxyHost,
    #     "port": proxyPort,
    # }
    proxies = {
        "http": proxyHttp,
        # "https": proxyHttps
    }
    ip_queue.put(proxies)
ip_queue = Queue()  # ip队列
get_ip_queue()

proxies=ip_queue.get()
print(proxies)
#响应头
res = requests.get(url, proxies=proxies, headers=header)
#发起请求
print(res.status_code) #返回响应码
