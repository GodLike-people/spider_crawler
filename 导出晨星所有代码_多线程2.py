#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :导出晨星代码所有isn码_待完成.py
# @Time     :2023/12/413:12
# @Author   :aczhang


"""
可以导出晨星网站所有的SecId，通过secId，再去反查isin码，或cx代码
"""
from itertools import count
from queue import Queue

import aiohttp
import pandas as pd
import requests
import json
import asyncio
import random
import re
import requests
import fake_useragent

# 下载晨星对应的cx_id，cx_code,isin对应数据
class MorningStarSpider:
    def __init__(self):
        self.excel_filename = "晨星信息表.xlsx"
        self.url="http://http.tiqu.alibabaapi.com/getip?num=1&type=2&pack=136012&port=1&lb=1&pb=4&regions="
        self.header={
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
            'authorization': '',
            'credentials': 'omit',
            'origin': 'https://www.morningstar.hk',
            'referer': 'https://www.morningstar.hk/hk/report/fund/portfolio.aspx?t=0P00001B6G&lang=en-HK',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        }
        # ip队列
        self.ip_queue=Queue()
        # 组装要请求的地址队列
        self.url_queue=Queue()
        # 请求地址，返回的response
        self.response_queue=Queue()
        # 对response 请求的详细数据
        self.detail_queue=Queue()
        # 记录权限的队列
        self.authorization_queue=Queue()

    def get_ip(self):
        res3 = requests.get(self.url)
        ip = json.loads(res3.text)['data'][0]
        proxyHost = ip["ip"]
        proxyPort = ip["port"]
        proxyHttp = "http://%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
        }
        proxies = {
            "http": proxyHttp,
        }
        self.ip_queue.put(proxies)

    def get_header(self):
        cx_code_list = ['0P00002C42', '0P00002C21', '0P0001H1ZQ', '0P0001H1ZG', '0P0001I2RK', '0P0001I2C4',
                        '0P0001I2RJ', '0P0001I2C3', '0P0001I3WN', '0P0001I3WL', '0P0001I3WO', '0P0001I3WM',
                        '0P0001IQSA', '0P00006SOO', '0P0001IGUS', '0P0001IH6G', '0P00006SON', '0P0001IMI6',
                        ]
        cx_code = random.choice(cx_code_list)
        url = f'https://www.morningstar.hk/hk/report/fund/performance.aspx?t={cx_code}&fundservcode=&lang=en-HK'
        res = requests.get(url)
        # 使用正则表达式提取maas_token后面的数据
        match = re.search(r'maas_token="([^"]+)"', res.text)
        if match:
            maas_token = match.group(1)
            # print(f"maas_token: {maas_token}")
            authorization="Bearer " + maas_token
            self.authorization_queue.put(authorization)

    def get_all_data(self):
        url = 'https://tools.morningstar.co.uk/api/rest.svc/roq2rh8blz/security/screener?page=1&pageSize=11000&sortOrder=LegalName%20asc&outputType=json&version=1&languageId=en-HK&currencyId=HKD&universeIds=FOHKG%24%24ALL&securityDataPoints=SecId%7CName%7CPriceCurrency%7CTenforeId%7CLegalName%7CClosePrice%7CYield_M12%7CCategoryName%7CMedalist_RatingNumber%7CStarRatingM255%7CSustainabilityRank%7CGBRReturnD1%7CGBRReturnW1%7CGBRReturnM1%7CGBRReturnM3%7CGBRReturnM6%7CGBRReturnM0%7CGBRReturnM12%7CGBRReturnM36%7CGBRReturnM60%7CGBRReturnM120%7CMaxFrontEndLoad%7COngoingCharge%7CManagerTenure%7CMaxDeferredLoad%7CInitialPurchase%7CFundTNAV%7CEquityStyleBox%7CBondStyleBox%7CAverageMarketCapital%7CAverageCreditQualityCode%7CEffectiveDuration%7CMorningstarRiskM255%7CAlphaM36%7CBetaM36%7CR2M36%7CStandardDeviationM36%7CSharpeM36%7CTrackRecordExtension&filters=&term=&subUniverseId='
        res = requests.get(url, verify=False)
        data_list = json.loads(res.text)['rows']
        return data_list

    def get_requests(self,data_list):
        if len(data_list)>0:
            for data in data_list:
                SecId = data['SecId']
                url2 = f'https://www.us-api.morningstar.com/sal/sal-service/fund/securityMetaData/{SecId}'
                self.url_queue.put(url2)

    #队列里的连接进行执行，收集返回的数据
    def get_response(self):
        self.get_ip()
        self.get_header()
        while True:
            # 取出ip
            proxy_ip=self.ip_queue.get()
            # header里的权限
            authorization=self.authorization_queue.get()
            # 取出url
            url = self.url_queue.get()
            # 确保代码在产生异常前调用task_done方法
            self.url_queue.task_done()
            #请求数据
            self.header["authorization"]=authorization
            try:
                response=requests.get(url,headers=self.header,proxies=proxy_ip,timeout=5)
                self.response_queue.put(response)
            except Exception as e:
                print(e)
            # 代理重用
            if response.status_code == 200:
                self.ip_queue.put(proxy_ip)
                self.authorization_queue.put(authorization)
                print('当前代理ip已请求成功:', proxy_ip)
            elif response.status_code == 401:
                # 把有问题的url再塞回队列
                self.get_header()
                self.url_queue.put(url)
                print('Authorization失效请重新提取,当前url为>>>>',url)
            else:
                self.url_queue.put(url)
                print('状态码异常...',url)
# 如果请求状态是401则重新请求get_header
# 如果网页请求失败，可以切换ip

    def parse_info(self):
        while True:
            response = self.response_queue.get()
            data=json.loads(response)
            secId=data.get("secId","")
            name=data.get("name","")
            cx_code=data.get("performanceId","")
            fundShareClassId=data.get("fundShareClassId","")
            assetType=data.get("assetType","")
            baseCurrencyId=data.get("baseCurrencyId","")
            countryId=data.get("countryId","")
            newAssetType=data.get("newAssetType","")
            domicileCountryId=data.get("domicileCountryId","")
            data_dic={
                "secId":secId,
                "name":name,
                "cx_code":cx_code,
                "fundShareClassId":fundShareClassId,
                "assetType":assetType,
                "baseCurrencyId":baseCurrencyId,
                "countryId":countryId,
                "newAssetType":newAssetType,
                "domicileCountryId":domicileCountryId
            }
            self.detail_queue.put(data_dic)
            self.response_queue.task_done()

    def save_info(self):
        while True:
            data_dic=self.detail_queue.get()
            # 将要存的数据为
            print('将要存储的数据为:', data_dic)
            self.detail_queue.task_done()
            df = pd.DataFrame([data_dic])
            # 追加模式写入Excel文件，不写入索引
            with pd.ExcelWriter(self.excel_filename, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                # 如果Excel文件中没有工作表，则创建一个
                if writer.book.sheet_names == []:
                    df.to_excel(writer, index=False)
                else:
                    # 如果工作表已存在，则将数据追加到工作表中
                    df.to_excel(writer, index=False,
                                startrow=len(writer.book.sheet_by_name(writer.sheet_names[0]).iter_rows()))
            # 将DataFrame写入Excel文件
            # df.to_excel(excel_filename, index=False)

if __name__ == '__main__':
    spider=MorningStarSpider()
    spider.get_header()

    print(spider.header)


