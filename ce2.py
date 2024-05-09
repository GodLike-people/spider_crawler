#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :ce2.py
# @Time     :2024/5/811:33
# @Author   :aczhang
import time
import random

import pymongo
import requests
import threading
from lxml import etree
from retrying import retry
from queue import Queue
from fake_useragent import UserAgent


class DangDangShop:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient()
        self.collection = self.mongo_client['py_spider']['dangdang_shop']
        self.url = 'https://search.dangdang.com/?key=python&act=input'
        self.headers = {
            'User-Agent': ''
        }
        self.ip_url = 'https://dps.kdlapi.com/api/getdps/?secret_id=oe7w9zhzlxsam81djbzq&num=1&signature=srd6psaxat37io1w5gw5avksxztvdsxd&pt=1&sep=1'

        self.ip_queue = Queue()  # ip队列
        self.url_queue = Queue()  # url队列
        self.response_queue = Queue()  # response队列
        self.detail_queue = Queue()  # 商品信息队列

    # 获取代理ip并上传到ip队列
    def get_ip(self):
        proxy_ip = requests.get(self.ip_url).text
        self.ip_queue.put(proxy_ip)

    def get_goods_index(self):
        response = requests.get(self.url, headers=self.headers)
        return response

    def get_page_num(self, response):
        tree = etree.HTML(response.text)
        max_page = tree.xpath("//ul[@name='Fy']/li[last()-2]/a/text()")[0]
        if max_page:
            for page in range(1, int(max_page) + 1):
                url = 'https://search.dangdang.com/?key=python&act=input&page_index={}'.format(page)
                self.url_queue.put(url)
        else:
            self.url_queue.put(self.url)

    @retry(stop_max_attempt_number=5)
    def get_goods_list(self):
        self.get_ip()
        while True:
            proxy_ip = self.ip_queue.get()
            url = self.url_queue.get()  # 如果请求失败则不会对失败的url重新请求, 会造成数据丢失的问题

            # 确保代码在产生异常前调用task_done方法
            self.url_queue.task_done()

            username = "代理用户名"
            password = "代理密码"
            proxies = {
                "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
                "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
            }
            self.headers['User-Agent'] = UserAgent().random
            response = requests.get(url, headers=self.headers, proxies=proxies, timeout=5)
            self.response_queue.put(response)

            # 代理重用
            if response.status_code == 200:
                self.ip_queue.put(proxy_ip)
                print('当前代理ip已请求成功:', proxy_ip)
            else:
                print('状态码异常...')

    def save_info(self):
        while True:
            detail = self.detail_queue.get()
            print('将要存储的数据为:', detail)
            self.collection.insert_one(detail)
            self.detail_queue.task_done()

    def parse_info(self):
        while True:
            response = self.response_queue.get()
            tree = etree.HTML(response.text)
            li_list = tree.xpath("//ul[@class='bigimg']/li")
            for li in li_list:
                item = dict()
                goods_name = li.xpath("./a/@title")
                goods_price = li.xpath("p[@class='price']/span[1]/text()")
                item['goods_name'] = goods_name[0]
                item['goods_price'] = goods_price[0] if goods_price else '空'
                self.detail_queue.put(item)
            self.response_queue.task_done()

    def main(self):
        response = self.get_goods_index()
        self.get_page_num(response)

        thread_list = list()
        for _ in range(5):
            thread_obj = threading.Thread(target=self.get_goods_list)
            thread_list.append(thread_obj)

        for _ in range(5):
            thread_obj = threading.Thread(target=self.parse_info)
            thread_list.append(thread_obj)

        save_thread = threading.Thread(target=self.save_info)
        thread_list.append(save_thread)

        for item in thread_list:
            item.daemon = True
            item.start()

        for queue in [self.url_queue, self.response_queue, self.detail_queue]:
            queue.join()


if __name__ == '__main__':
    dd_shop = DangDangShop()
    dd_shop.main()

