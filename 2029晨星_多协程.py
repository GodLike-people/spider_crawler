#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2029晨星.py
# @Time     :2024/5/713:26
# @Author   :aczhang
import json
import random

import aiohttp
import pandas as pd
import requests
import re
from dateutil import parser as date_parser
from twisted.plugins.twisted_reactors import asyncio


def get_mass_token(cx_code):
    url=f'https://www.morningstar.hk/hk/report/fund/performance.aspx?t={cx_code}&fundservcode=&lang=en-HK'
    res=requests.get(url)
    # 使用正则表达式提取maas_token后面的数据
    match = re.search(r'maas_token="([^"]+)"', res.text)
    if match:
        maas_token = match.group(1)
        # print(f"maas_token: {maas_token}")
        return maas_token

def get_secIds():
    # 读取Excel文件
    df = pd.read_excel('晨星id汇总.xlsx')
    # 假设SecId字段在Excel中的名字就是SecId，如果不是，需要替换成实际的列名
    sec_ids = df['SecId'].tolist()
    return sec_ids


cx_code_list = ['0P00002C42', '0P00002C21', '0P0001H1ZQ', '0P0001H1ZG', '0P0001I2RK', '0P0001I2C4', '0P0001I2RJ', '0P0001I2C3', '0P0001I3WN', '0P0001I3WL', '0P0001I3WO', '0P0001I3WM', '0P0001IQSA', '0P00006SOO', '0P0001IGUS', '0P0001IH6G', '0P00006SON', '0P0001IMI6', '0P0001IMNI', '0P0001J6MJ', '0P0001J6MH', '0P0001J6MM', '0P0001J6MK', '0P0001J6ME', '0P0001J6MC', '0P0001K9T2', '0P0001K9DO', '0P0001K57J', '0P0001K2V8', '0P0001K57I', '0P0001KFZU', '0P0001KFUA', '0P0001KIKG', '0P0001KIKH', '0P0001KIKI', '0P0001KIKJ', '0P0001KQJ7', '0P0001KQJ9', '0P0001LX8A', '0P0001LX8B', '0P0001M4LA', '0P0001M4JT', '0P0001M4L9', '0P0001M4LG', '0P0001M4JS', '0P0001M4LH', '0P0001MIGF', '0P0001MKPP', '0P0001MKPJ', '0P0001P25B', '0P0001P25A', '0P0001OWSY', '0P0001MZW7', '0P0001MZW8', '0P0001MZW6', '0P0001OE1M', '0P0001OE1N', '0P0001MZWD', '0P0001N4PY']
cx_code = random.choice(cx_code_list)
maas_token = get_mass_token(cx_code)

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'Authorization':'Bearer '+maas_token,
    # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EY3hOemRHTnpGRFJrSTRPRGswTmtaRU1FSkdOekl5TXpORFJrUTROemd6TWtOR016bEdOdyJ9.eyJodHRwczovL21vcm5pbmdzdGFyLmNvbS9tc3Rhcl9pZCI6Ijc2NjU2NkFELTkxMjEtNDJDMS05RjM2LTkwREM1RkNENUUxQyIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL3Bhc3N3b3JkQ2hhbmdlUmVxdWlyZWQiOmZhbHNlLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9lbWFpbCI6Imo2M2s4OTVuanBhOG1ubXE0cDJqbXN0dGNoOTBzYWhiQG1hYXMtbXN0YXIuY29tIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcm9sZSI6WyJFQy5TZXJ2aWNlLkNvbmZpZ3VyYXRpb24iLCJFQy5TZXJ2aWNlLkhvc3RpbmciLCJFQ1VTLkFQSS5BdXRvY29tcGxldGUiLCJFQ1VTLkFQSS5TY3JlZW5lciIsIkVDVVMuQVBJLlNlY3VyaXRpZXMiLCJQQUFQSVYxLlhyYXkiLCJWZWxvVUkuQWxsb3dBY2Nlc3MiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vY29tcGFueV9pZCI6IjI4MmNjODY1LTM1MDUtNGUyMC04ZDI0LTg0YTQzOGIyMTkyNCIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2ludGVybmFsX2NvbXBhbnlfaWQiOiJDbGllbnQwIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vZGF0YV9yb2xlIjpbIkVDVVMuRGF0YS5VUy5PcGVuRW5kRnVuZHMiLCJRUy5NYXJrZXRzIiwiUVMuUHVsbHFzIiwiU0FMLlNlcnZpY2UiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vbGVnYWN5X2NvbXBhbnlfaWQiOiIyNGJmMGE4NS0zMjcxLTRiMWItYWIxZS0wZTlmZDE4ODE4YmQiLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS91aW1fcm9sZXMiOiJFQU1TLE1VX01FTUJFUl8xXzEiLCJpc3MiOiJodHRwczovL2xvZ2luLXByb2QubW9ybmluZ3N0YXIuY29tLyIsInN1YiI6ImF1dGgwfDc2NjU2NkFELTkxMjEtNDJDMS05RjM2LTkwREM1RkNENUUxQyIsImF1ZCI6WyJodHRwczovL2F1dGgwLWF3c3Byb2QubW9ybmluZ3N0YXIuY29tL21hYXMiLCJodHRwczovL3VpbS1wcm9kLm1vcm5pbmdzdGFyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTUwNTk4NzQsImV4cCI6MTcxNTA2MzQ3NCwic2NvcGUiOiJvcGVuaWQiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6ImlRa1d4b2FwSjlQeGw4Y0daTHlhWFpzYlhWNzlnNjRtIn0.Tf6zdOIn3QTt21nRAcj62GWWd4oiDCLprL5w5GwX3c9l4M17-mbr-yM-Qlle1keVJ5O7Y3VMfl9lymak2hWPwHiPvbMowfu7lFXafOTL_89v_XFEPWrVL1ygClkXcqhvhLf3Ck8IDkHgq-dJ9CFac09OJOysgGnxDfszlBvsAHii56597GEya5UMTJ3mJHr8inSK2GmjCn1RQNMIV-es_z35z4qVL3egs2P6csdB4yW6udysHLnR6Wqrx9G6q9dlvXOOUZDeWFPy-euIXBQ7QyfNE3C8dmb8vMUMyc9GWagEuTTRVDQzgvOEFddyNfSgaT1HYFsTKryX-KhDL4d4CA',
    'credentials': 'omit',
    'origin': 'https://www.morningstar.hk',
    'priority': 'u=1, i',
    'referer': 'https://www.morningstar.hk/hk/report/fund/portfolio.aspx?t=0P0001QTJK&lang=en-HK',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
}

params = {
    'premiumNum': '100',
    'freeNum': '25',
    'languageId': 'en',
    'locale': 'en',
    'clientId': 'MDC_intl',
    'benchmarkId': 'mstarorcat',
    'component': 'sal-components-mip-holdings',
    'version': '3.60.0',
}

def get_url(secIds):
    url_list = []
    for secId in secIds:
        url=f'https://www.us-api.morningstar.com/sal/sal-service/fund/portfolio/holding/v2/{secId}/data'
        url_list.append(url)
    return url_list

def parse_date(date_str):
    # 使用dateutil解析日期字符串
    date_obj = date_parser.parse(date_str)

    # 格式化日期为所需的格式
    formatted_date = date_obj.strftime("%Y%m%d")
    return formatted_date

secIds=get_secIds()
# 组装好所有持仓数据的url
url_list=get_url(secIds)

fund_list = []

async def fetch_fund_data(session, url, params, headers):
    async with session.get(url, params=params, headers=headers) as response:
        data = await response.text()
        return json.loads(data)

async def process_fund_data(data):
    # EQUITY 股票
    fund_type = data.get("assetType")
    # NZD 货币
    baseCurrency = data.get("baseCurrencyId")
    # secId : "F00001FHRC"
    cx_code = data.get("secId")
    # 持仓最新日期
    holding_date = parse_date(data.get("portfolioLastestDateFooter"))
    # 持仓数据
    holdingList = data.get("equityHoldingPage").get("holdingList")

    # 持仓数据清洗
    holding_list = []
    for holding in holdingList:
        isin = holding.get("isin", "")
        country = holding.get("country", "")
        securityName = holding.get("securityName", "")
        stockRating = holding.get("stockRating", "")
        weighting = holding.get("weighting", "")
        sector = holding.get("sector", "")
        ticker = holding.get("ticker", "")

        data_dic = {
            "holding_isin": isin,
            "country": country,
            "securityName": securityName,
            'stockRating': stockRating,
            'weighting': weighting,
            'sector': sector,
            'ticker': ticker,
        }

        holding_list.append(data_dic)

    fund_data_dic = {
        "cx_code": cx_code,
        'fund_type': fund_type,
        'baseCurrency': baseCurrency,
        'holding_date': holding_date,
        "holdingList": holding_list
    }
    print(fund_data_dic)

    return fund_data_dic

async def main(url_list, params, headers):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_fund_data(session, url, params, headers) for url in url_list]
        datas = await asyncio.gather(*tasks)
        fund_list = [await process_fund_data(data) for data in datas]
        return fund_list


# 运行主函数并获取结果
asyncio.run(main(url_list, params, headers))

loop = asyncio.get_event_loop()
try:
    fund_list = loop.run_until_complete(main(url_list, params, headers))
finally:
    loop.close()

# 将多组json数据转换为DataFrame
df = pd.json_normalize(
    fund_list,
    'holdingList',
    # 参数为holdingList中的每个字段名前添加了前缀holding
    record_prefix='holding',
    meta=[
        'cx_code',  # 直接将cx_code作为列添加
        'holding_date'  # 将holding_date转换为字符串格式后作为列添加
    ],
    errors='ignore'  # 如果有错误则忽略
)
# 将DataFrame写入Excel文件
df.to_excel('2029holdings.xlsx', index=False)
