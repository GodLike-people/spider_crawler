#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :导出晨星代码所有isn码_待完成.py
# @Time     :2023/12/413:12
# @Author   :aczhang


"""
可以导出晨星网站所有的SecId，通过secId，再去反查isin码，或cx代码
"""
from itertools import count

import aiohttp
import pandas as pd
import requests
import json
import asyncio
import random
import re

#coding=utf-8
import requests

def get_ip_list(num):
    #请求地址
    # url3=f'http://http.tiqu.alibabaapi.com/getip3?num={num}&type=2&pack=129761&port=1&lb=1&pb=45&gm=4&regions='
    url3=f'http://http.tiqu.alibabaapi.com/getip?num={num}&type=2&pack=136012&port=1&lb=1&pb=45&regions='

    res3=requests.get(url3)

    ip_list=json.loads(res3.text)['data']
    #把所有ip组成一个list，在选择的时候随机选
    ip_list_last=[]

    for ip in ip_list:
        # 代理服务器
        proxyHost = ip["ip"]
        proxyPort = ip["port"]
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
        ip_list_last.append(proxies)

    return ip_list_last

def generate_random_string():
    result = ""
    for n in range(1, 33):
        result += format(random.randint(0, 15), 'x')
        if n in [8, 12, 16, 20]:
            result += "-"
    return result

def get_mass_token(cx_code):
    url=f'https://www.morningstar.hk/hk/report/fund/performance.aspx?t={cx_code}&fundservcode=&lang=en-HK'
    res=requests.get(url)

    # 使用正则表达式提取maas_token后面的数据
    match = re.search(r'maas_token="([^"]+)"', res.text)

    if match:
        maas_token = match.group(1)
        # print(f"maas_token: {maas_token}")
        return maas_token

cx_code_list = ['0P00002C42', '0P00002C21', '0P0001H1ZQ', '0P0001H1ZG', '0P0001I2RK', '0P0001I2C4', '0P0001I2RJ', '0P0001I2C3', '0P0001I3WN', '0P0001I3WL', '0P0001I3WO', '0P0001I3WM', '0P0001IQSA', '0P00006SOO', '0P0001IGUS', '0P0001IH6G', '0P00006SON', '0P0001IMI6', '0P0001IMNI', '0P0001J6MJ', '0P0001J6MH', '0P0001J6MM', '0P0001J6MK', '0P0001J6ME', '0P0001J6MC', '0P0001K9T2', '0P0001K9DO', '0P0001K57J', '0P0001K2V8', '0P0001K57I', '0P0001KFZU', '0P0001KFUA', '0P0001KIKG', '0P0001KIKH', '0P0001KIKI', '0P0001KIKJ', '0P0001KQJ7', '0P0001KQJ9', '0P0001LX8A', '0P0001LX8B', '0P0001M4LA', '0P0001M4JT', '0P0001M4L9', '0P0001M4LG', '0P0001M4JS', '0P0001M4LH', '0P0001MIGF', '0P0001MKPP', '0P0001MKPJ', '0P0001P25B', '0P0001P25A', '0P0001OWSY', '0P0001MZW7', '0P0001MZW8', '0P0001MZW6', '0P0001OE1M', '0P0001OE1N', '0P0001MZWD', '0P0001N4PY']

"""
单个数据的提取
"""
def fetch_data(ip_list_last, data):
    SecId = data['SecId']
    # Name=data['Name']
    TenforeId = data.get("TenforeId", "")
    Name = data.get("Name", "")
    cx_code = random.choice(cx_code_list)
    maas_token = get_mass_token(cx_code)

    header = {
        'Authorization':'Bearer '+maas_token,
        'Referer':
            'https://www.morningstar.hk/hk/report/fund/performance.aspx?t=0P0000NO9V&lang=en-HK',
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',

        'X-Api-Realtime-E':
            'eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.jidbnhWUJvWMvD2omPxv9L_-iiW424c89SMUexsXDrY3VE6CfIU1g6cRPZ-DToeSbtFEvMPV4DoNlOtzUJ63Ryja23rtjlMsrpV-nLpUUpjcZp7ZL0YjGQNbsq1a-vAwf7GBOk6lnsOWycXB0mKaHMXfHpgwAsRcfGK1QpIb27U.da0qHJBnRmc0_EOq.1fXioE66EIItzsggPK3b4HNypNp1Ltva84HWRNmxwBPsUo5kvUXaYDuFjLHT2K39RsoMqZzERuQMfrP8fYoqTfkBmg-xD5sQbqHYeKgvuqMdOlkRVx4y16ft1RiliknyWNGxTd_5KXZrkDadGR7gHQyC775iNEBi0bI9F_JXu3t7_8uBMHNOYlIeRHm2Dqmz17ukL_zoGOX74_KiaYkBL5RamA.7wz-dbBZR15KCDRanQrHPg',

        'X-Api-Requestid':
            generate_random_string(),

        'X-Sal-Contenttype':
            'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='

    }
    # print(header)
    # print(ip_list_last)
    ip2 = random.choice(ip_list_last)
    url2 = f'https://www.us-api.morningstar.com/sal/sal-service/fund/securityMetaData/{SecId}'
    # res = requests.get(url2, headers=header)
    res2 = requests.get(url2, headers=header,proxies=ip2)
    print(res2.status_code)
    # print(res2.text)
    if res2.text:
        json_data = json.loads(res2.text)
        cx_code = json_data.get("performanceId", "")
        isin = json_data.get("isin", "")
        secId = json_data.get("secId", "")
        baseCurrencyId = json_data.get("baseCurrencyId", "")
        data_dic = {
            'cx_code': cx_code,
            'isin': isin,
            'Name': Name,
            'baseCurrencyId': baseCurrencyId,
            'secId': secId,
            'SecId': SecId,
        }
        print(data_dic)
        return data_dic

def get_all_data():
    url = 'https://tools.morningstar.co.uk/api/rest.svc/roq2rh8blz/security/screener?page=1&pageSize=11000&sortOrder=LegalName%20asc&outputType=json&version=1&languageId=en-HK&currencyId=HKD&universeIds=FOHKG%24%24ALL&securityDataPoints=SecId%7CName%7CPriceCurrency%7CTenforeId%7CLegalName%7CClosePrice%7CYield_M12%7CCategoryName%7CMedalist_RatingNumber%7CStarRatingM255%7CSustainabilityRank%7CGBRReturnD1%7CGBRReturnW1%7CGBRReturnM1%7CGBRReturnM3%7CGBRReturnM6%7CGBRReturnM0%7CGBRReturnM12%7CGBRReturnM36%7CGBRReturnM60%7CGBRReturnM120%7CMaxFrontEndLoad%7COngoingCharge%7CManagerTenure%7CMaxDeferredLoad%7CInitialPurchase%7CFundTNAV%7CEquityStyleBox%7CBondStyleBox%7CAverageMarketCapital%7CAverageCreditQualityCode%7CEffectiveDuration%7CMorningstarRiskM255%7CAlphaM36%7CBetaM36%7CR2M36%7CStandardDeviationM36%7CSharpeM36%7CTrackRecordExtension&filters=&term=&subUniverseId='
    res = requests.get(url, verify=False)
    # print(res.text)
    data_list = json.loads(res.text)['rows']
    return data_list

def excel_output_280(last_all_list):
    df = pd.DataFrame(last_all_list)

    # 将数据追加到一个不存在的Excel表格
    excel_file_path = '导出晨星代码(最新).xlsx'  # 替换为你想要保存的Excel文件的路径

    # 使用try-except块以处理表格不存在的情况
    try:
        # 尝试读取现有表格
        existing_df = pd.read_excel(excel_file_path)

        # 如果表格存在，将新数据追加到现有数据后面
        updated_df = existing_df.append(df, ignore_index=True)

    except FileNotFoundError:
        # 如果表格不存在，直接保存新数据
        updated_df = df

    # 将更新后的数据保存到Excel表格
    updated_df.to_excel(excel_file_path, index=False)

    print(f"已成功保存{len(last_all_list)}条数据--", excel_file_path)

def main():
    #1 获取所有要处理的数据的  'secId': 'F00000QGDB'
    data_list=get_all_data()
    print(len(data_list))

    #2 获取代理ip
    ip_list_last = get_ip_list(1)
    print(ip_list_last)
    # 设定重新获取 IP 列表的阈值
    refresh_threshold = 300
    refresh_counter = 0
    count=0
    last_all_list = []
    for data in data_list:
        if refresh_counter >= refresh_threshold:
            # 输出数据
            excel_output_280(last_all_list)
            # 重新获取 IP 列表
            ip_list_last =get_ip_list(1)
            print(ip_list_last)
            last_all_list = []
            refresh_counter = 0  # 重置计数器
        refresh_counter += 1
        count+=1
        data_dic=fetch_data(ip_list_last, data)
        last_all_list.append(data_dic)
        print(f"第{count}个数据，继续执行！")
    excel_output_280(last_all_list)

main()

