#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :代理.py
# @Time     :2024/5/716:48
# @Author   :aczhang
import json

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, as_completed

url = 'https://movie.douban.com/top250?start={}&filter='

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def get_movie_info(page):
    response = requests.get(url.format(page * 25), headers=headers).text
    tree = etree.HTML(response)
    result = tree.xpath("//div[@class='hd']/a/span[1]/text()")
    return result


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(get_movie_info, page) for page in range(10)]
        # future对象获取返回值会造成主线程堵塞
        # for future in futures:
        #     print(future.result())

        # as_completed会立即返回处理完成的结果而不会堵塞主线程
        for future in as_completed(futures):
            print(future.result())

