#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2029晨星.py
# @Time     :2024/5/713:26
# @Author   :aczhang
import json
import random
from queue import Queue

import pandas as pd
import requests
import re
from dateutil import parser as date_parser
from datetime import datetime
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

def get_ip_list(num):
    #请求地址
    # url3=f'http://http.tiqu.alibabaapi.com/getip3?num={num}&type=2&pack=129761&port=1&lb=1&pb=45&gm=4&regions='
    url3 = f'http://http.tiqu.alibabaapi.com/getip?num={num}&type=2&pack=136012&port=1&lb=1&pb=4&regions='
    # http: // http.tiqu.alibabaapi.com / getip?num = 10 & type = 2 & pack = 136012 & port = 1 & lb = 1 & pb = 4 & regions =

    res3 = requests.get(url3)
    ip_list = json.loads(res3.text)['data']
    # 把所有ip组成一个list，在选择的时候随机选
    ip_list_last = []

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

# 59.60.121.185:4315

"""
获取一个新ip
"""
ip_queue = Queue()  # ip队列
def get_ip_queue():
    url3 = f'http://http.tiqu.alibabaapi.com/getip?num=1&type=2&pack=136012&port=1&lb=1&pb=45&regions='
    res3 = requests.get(url3)
    ip = json.loads(res3.text)['data']
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
    ip_queue.put(proxies)

def get_url(secIds):
    url_list = []
    for secId in secIds:
        url=f'https://www.us-api.morningstar.com/sal/sal-service/fund/portfolio/holding/v2/{secId}/data'
        data_dic={
            "secId": secId,
            'url':url,
            # 默认状态是0,0为未检查，1为数据成功录入，2为数据录入失败
            'status':0
        }
        url_list.append(data_dic)
    return url_list

def parse_date(date_str):
    # 检查输入是否为None
    if date_str is None:
        return None

    # 使用dateutil解析日期字符串
    date_obj = date_parser.parse(date_str)

    # 格式化日期为所需的格式
    formatted_date = date_obj.strftime("%Y%m%d")
    return formatted_date

"""
把所有数据，都记录下来
先判断excel里是否有数据，没有则下载所有，如果有则获取所有数据，并筛选出staus为0的数据
"""

# 读取Excel文件的函数
def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"读取Excel文件时发生错误：{e}")
        return None

# 将下载的数据写入Excel文件的函数
def write_data_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"数据已写入Excel文件：{file_path}")

# Excel文件路径
excel_file_path = '所有url数据汇总.xlsx'
# 检查Excel文件是否有数据
df = read_excel_file(excel_file_path)

url_list=[]
if df is None or df.empty:
    # excel 读取数据为空，写入数据
    secIds = get_secIds()
    # 组装好所有持仓数据的url
    url_list = get_url(secIds)
    # 先把所有的url放到excel里
    df3 = pd.DataFrame(url_list)
    # 将 DataFrame 写入 Excel 文件
    df3.to_excel('所有url数据汇总.xlsx', index=False)
else:
    # excel 有数据，进行筛选
    # 将DataFrame转换为字典格式
    data_dict = df.to_dict(orient='records')
    # 使用列表推导式筛选出 status 不为 1 的数据
    url_list = [record for record in data_dict if record['status'] != 1]
    # print(url_list)


def excel_output_exist(last_all_list,excel_file_path):
    df = pd.DataFrame(last_all_list)
    # 将数据追加到一个不存在的Excel表格
    # excel_file_path = '导出晨星代码(最新).xlsx'  # 替换为你想要保存的Excel文件的路径
    # 使用try-except块以处理表格不存在的情况
    try:
        # 尝试读取现有表格
        existing_df = pd.read_excel(excel_file_path)
        # 如果表格存在，将新数据追加到现有数据后面
        updated_df = existing_df.append(df, ignore_index=True)
    except FileNotFoundError:
        # 如果表格不存在，直接保存新数据
        updated_df = df
    # 去除重复的行，keep='first'表示保留重复行中的第一行
    df_unique = updated_df.drop_duplicates(subset='url',keep='first')
    # 将更新后的数据保存到Excel表格
    df_unique.to_excel(excel_file_path, index=False)

    # print(f"已成功保存{len(last_all_list)}条数据--", excel_file_path)
# 专用追加
def excel_output_append(fund_list,excel_file_path):
    # 检查Excel文件是否有数据
    df = read_excel_file(excel_file_path)

    if df is None or df.empty:
        # # # 将多组json数据转换为DataFrame
        df = pd.json_normalize(
            fund_list,
            'holdingList',
            # 参数为holdingList中的每个字段名前添加了前缀holding
            record_prefix='holding_',
            meta=[
                'cx_code',  # 直接将cx_code作为列添加
                'holding_date'  # 将holding_date转换为字符串格式后作为列添加
            ],
            errors='ignore'  # 如果有错误则忽略
        )
        df = df[['cx_code', 'holding_date'] + [col for col in df.columns if col not in ['cx_code', 'holding_date']]]
        # 将DataFrame写入Excel文件
        df.to_excel(excel_file_path, index=False)
    else:
        # 新追加的df
        new_df = pd.json_normalize(
            fund_list,
            'holdingList',
            # 参数为holdingList中的每个字段名前添加了前缀holding
            record_prefix='holding_',
            meta=[
                'cx_code',  # 直接将cx_code作为列添加
                'holding_date'  # 将holding_date转换为字符串格式后作为列添加
            ],
            errors='ignore'  # 如果有错误则忽略
        )
        new_df = new_df[['cx_code', 'holding_date'] + [col for col in df.columns if col not in ['cx_code', 'holding_date']]]

        # # 使用ExcelWriter以追加模式打开文件
        # with pd.ExcelWriter(excel_file_path, mode='a', engine='openpyxl') as writer:
        #     # 将新的DataFrame追加到Excel文件末尾
        #     new_data.to_excel(writer, index=False, header=False, startrow=df_existing.last_valid_index() + 1)
        # 如果表格存在，将新数据追加到现有数据后面
        updated_df = df.append(new_df, ignore_index=True)
        # excel 有数据，进行追加
        # 去除重复的行，keep='first'表示保留重复行中的第一行
        # df_unique = updated_df.drop_duplicates(subset='url', keep='first')
        # 将更新后的数据保存到Excel表格
        updated_df.to_excel(excel_file_path, index=False)
        print("追加数据成功!")

def excel_output(err_list,finished_list,fund_list):
    excel_output_exist(err_list,'出错url汇总.xlsx')
    # df1 = pd.DataFrame(err_list)
    # # 将 DataFrame 写入 Excel 文件
    # df1.to_excel('出错url汇总.xlsx', index=False)

    excel_output_exist(finished_list, '已完成汇总.xlsx')
    # df2 = pd.DataFrame(finished_list)
    # # 将 DataFrame 写入 Excel 文件
    # df2.to_excel('已完成汇总.xlsx', index=False)
    excel_output_append(fund_list, '2029holdings_2.xlsx')

def process_data(data):
    """
    当前基金数据
    """
    # EQUITY 股票
    fund_type = data.get("assetType")
    # NZD 货币
    baseCurrency = data.get("baseCurrencyId")
    # secId : "F00001FHRC"
    cx_code = data.get("secId")
    # print(cx_code)
    # 持仓最新日期
    holding_date = parse_date(data.get("portfolioLastestDateFooter"))
    # print(holding_date)
    # 股票持仓数据
    equityHolding = data.get("equityHoldingPage").get("holdingList")
    # print(equityHolding)
    # 债券持仓数据
    boldHoldingPage = data.get("boldHoldingPage").get("holdingList")
    # print(boldHoldingPage)
    # 其他持仓数据
    otherHoldingPage = data.get("otherHoldingPage").get("holdingList")
    # print(otherHoldingPage)

    holdingList = []
    # 持仓数据清洗
    equity_holding_list = []
    if len(equityHolding) > 0:
        for holding in equityHolding:
            """
            持仓数据
            """
            # 当前持仓的isin码与基金无关
            isin = holding.get("isin", "")
            # 当前持仓的晨星码与基金无关
            # secId=holding.get("secId")
            # 当前持仓所属国家
            country = holding.get("country", "")
            # 持仓类型 holdingType: "Equity"
            holdingType = holding.get("holdingType", "")
            # 持仓名称 Tencent Holdings Ltd
            securityName = holding.get("securityName", "")
            # 星级
            stockRating = holding.get("stockRating", "")
            # 份额
            weighting = holding.get("weighting", "")
            # 行业
            sector = holding.get("sector", "")
            # 当前持仓 对应代码
            ticker = holding.get("ticker", "")

            data_dic = {
                "equity_holding_isin": isin,
                "equity_country": country,
                "equity_securityName": securityName,
                'equity_stockRating': stockRating,
                'equity_weighting': weighting,
                'equity_sector': sector,
                'equity_ticker': ticker,
                'equity_holdingType': holdingType
            }
            equity_holding_list.append(data_dic)
        holdingList.extend(equity_holding_list)

    bond_holding_list = []
    if len(boldHoldingPage) > 0:
        for holding in boldHoldingPage:
            """
            持仓数据
            """
            # 当前持仓的isin码与基金无关
            isin = holding.get("isin", "")
            # 当前持仓的晨星码与基金无关
            # secId=holding.get("secId")
            # 当前持仓所属国家
            country = holding.get("country", "")
            # 持仓类型 holdingType:  "Bond"
            holdingType = holding.get("holdingType", "")
            # 持仓名称 Tencent Holdings Ltd
            securityName = holding.get("securityName", "")
            # 星级
            stockRating = holding.get("stockRating", "")
            # 份额
            weighting = holding.get("weighting", "")
            # 当前持仓 对应代码
            # ticker = holding.get("ticker", "")
            # 债券结束日期
            maturityDate = parse_date(holding.get("maturityDate", ""))
            # 主要分类
            primarySectorName = holding.get("primarySectorName", "")
            # 二级分类
            secondarySectorName = holding.get("secondarySectorName", "")

            data_dic = {
                "bond_holding_isin": isin,
                "bond_country": country,
                "bond_securityName": securityName,
                'bond_stockRating': stockRating,
                'bond_weighting': weighting,
                # 'bond_ticker': ticker,
                'bond_holdingType': holdingType,
                'bond_maturityDate': maturityDate,
                # "bond_sector": superSectorName,
                "bond_primarySectorName": primarySectorName,
                "bond_secondarySectorName": secondarySectorName
            }
            bond_holding_list.append(data_dic)
        holdingList.extend(bond_holding_list)

    other_holding_list = []
    if len(otherHoldingPage) > 0:
        for holding in otherHoldingPage:
            """
            持仓数据
            """
            # 当前持仓的isin码与基金无关
            isin = holding.get("isin", "")
            # 当前持仓的晨星码与基金无关
            # secId=holding.get("secId")
            # 当前持仓所属国家
            country = holding.get("country", "")
            # 持仓类型 "Other"
            holdingType = holding.get("holdingType", "")
            # 持仓名称 Tencent Holdings Ltd
            securityName = holding.get("securityName", "")
            # 份额
            weighting = holding.get("weighting", "")
            # 当前持仓 对应代码
            # ticker = holding.get("ticker", "")
            # 主要分类
            primarySectorName = holding.get("primarySectorName", "")
            # 二级分类
            secondarySectorName = holding.get("secondarySectorName", "")
            # 债券结束日期
            maturityDate = parse_date(holding.get("maturityDate", ""))
            # 债券行业
            superSectorName = holding.get("superSectorName", "")

            data_dic = {
                "other_holding_isin": isin,
                "other_country": country,
                "other_securityName": securityName,
                'other_primarySectorName': primarySectorName,
                'other_secondarySectorName': secondarySectorName,
                'other_weighting': weighting,
                # 'other_ticker': ticker,
                'other_holdingType': holdingType,
                'other_maturityDate': maturityDate,
                "other_sector": superSectorName
            }
            other_holding_list.append(data_dic)
        holdingList.extend(other_holding_list)

    fund_data_dic = {
        "cx_code": cx_code,
        'fund_type': fund_type,
        'baseCurrency': baseCurrency,
        'holding_date': holding_date,
        "holdingList": holdingList
    }

    print(fund_data_dic)
    fund_list.append(fund_data_dic)
    return fund_list

fund_list = []
err_list=[]
finished_list=[]
ip_list_last = get_ip_list(1)
# get_ip_queue()

try:
    # 设定重新获取 IP 列表的阈值
    refresh_threshold = 250
    refresh_counter = 0
    for index, url in enumerate(url_list):
        print(f"运行的第{index}次")
    # 更换持仓的cxid后的url
        if refresh_counter >= refresh_threshold:
            # 重新获取 IP 列表
            ip_list_last = get_ip_list(1)
            last_all_list = []
            refresh_counter = 0  # 重置计数器
        refresh_counter += 1

        url_current=url.get("url","")
        status=url.get("status","")
        # data=dict()
        try:
            ip2 = random.choice(ip_list_last)
            print('当前代理ip已请求成功:', ip2)
            # ip2=ip_queue.get()
            response = requests.get(
                url_current,
                params=params,
                headers=headers,
                proxies=ip2,
                timeout=(3,7)
            )
            print(response.status_code)
            data = json.loads(response.text)
            # ip_queue.put(ip2)
            # print(data)
        except Exception as e:
            err_data = {
                "url": url,
                "err": e,
                "date":datetime.now()
            }
            url.update({'status': 2})
            err_list.append(err_data)
            # 存错误数据
            excel_output_exist(err_list,"url_error.xlsx")
            # 存现有数据
            excel_output_append(fund_list,"2029holdings_2.xlsx")
            # 处理HTTP请求错误，比如404或500等
            print(f'错误信息: {e}')


        """
        当前基金数据
        """

        # EQUITY 股票
        fund_type = data.get("assetType")
        # NZD 货币
        baseCurrency = data.get("baseCurrencyId")
        # secId : "F00001FHRC"
        cx_code = data.get("secId")
        # print(cx_code)
        # 持仓最新日期
        holding_date = parse_date(data.get("portfolioLastestDateFooter"))
        # print(holding_date)
        # 股票持仓数据
        equityHolding = data.get("equityHoldingPage").get("holdingList")
        # print(equityHolding)
        # 债券持仓数据
        boldHoldingPage = data.get("boldHoldingPage").get("holdingList")
        # print(boldHoldingPage)
        # 其他持仓数据
        otherHoldingPage = data.get("otherHoldingPage").get("holdingList")
        # print(otherHoldingPage)

        holdingList = []
        # 持仓数据清洗
        equity_holding_list = []
        if len(equityHolding) > 0:
            for holding in equityHolding:
                """
                持仓数据
                """
                # 当前持仓的isin码与基金无关
                isin = holding.get("isin", "")
                # 当前持仓的晨星码与基金无关
                # secId=holding.get("secId")
                # 当前持仓所属国家
                country = holding.get("country", "")
                # 持仓类型 holdingType: "Equity"
                holdingType = holding.get("holdingType", "")
                # 持仓名称 Tencent Holdings Ltd
                securityName = holding.get("securityName", "")
                # 星级
                stockRating = holding.get("stockRating", "")
                # 份额
                weighting = holding.get("weighting", "")
                # 行业
                sector = holding.get("sector", "")
                # 当前持仓 对应代码
                ticker = holding.get("ticker", "")

                data_dic = {
                    "equity_holding_isin": isin,
                    "equity_country": country,
                    "equity_securityName": securityName,
                    'equity_stockRating': stockRating,
                    'equity_weighting': weighting,
                    'equity_sector': sector,
                    'equity_ticker': ticker,
                    'equity_holdingType': holdingType
                }
                equity_holding_list.append(data_dic)
            holdingList.extend(equity_holding_list)

        bond_holding_list = []
        if len(boldHoldingPage) > 0:
            for holding in boldHoldingPage:
                """
                持仓数据
                """
                # 当前持仓的isin码与基金无关
                isin = holding.get("isin", "")
                # 当前持仓的晨星码与基金无关
                # secId=holding.get("secId")
                # 当前持仓所属国家
                country = holding.get("country", "")
                # 持仓类型 holdingType:  "Bond"
                holdingType = holding.get("holdingType", "")
                # 持仓名称 Tencent Holdings Ltd
                securityName = holding.get("securityName", "")
                # 星级
                stockRating = holding.get("stockRating", "")
                # 份额
                weighting = holding.get("weighting", "")
                # 当前持仓 对应代码
                # ticker = holding.get("ticker", "")
                # 债券结束日期
                maturityDate = parse_date(holding.get("maturityDate", ""))
                # 主要分类
                primarySectorName = holding.get("primarySectorName", "")
                # 二级分类
                secondarySectorName = holding.get("secondarySectorName", "")

                data_dic = {
                    "bond_holding_isin": isin,
                    "bond_country": country,
                    "bond_securityName": securityName,
                    'bond_stockRating': stockRating,
                    'bond_weighting': weighting,
                    # 'bond_ticker': ticker,
                    'bond_holdingType': holdingType,
                    'bond_maturityDate': maturityDate,
                    # "bond_sector": superSectorName,
                    "bond_primarySectorName": primarySectorName,
                    "bond_secondarySectorName": secondarySectorName
                }
                bond_holding_list.append(data_dic)
            holdingList.extend(bond_holding_list)

        other_holding_list = []
        if len(otherHoldingPage) > 0:
            for holding in otherHoldingPage:
                """
                持仓数据
                """
                # 当前持仓的isin码与基金无关
                isin = holding.get("isin", "")
                # 当前持仓的晨星码与基金无关
                # secId=holding.get("secId")
                # 当前持仓所属国家
                country = holding.get("country", "")
                # 持仓类型 "Other"
                holdingType = holding.get("holdingType", "")
                # 持仓名称 Tencent Holdings Ltd
                securityName = holding.get("securityName", "")
                # 份额
                weighting = holding.get("weighting", "")
                # 当前持仓 对应代码
                # ticker = holding.get("ticker", "")
                # 主要分类
                primarySectorName = holding.get("primarySectorName", "")
                # 二级分类
                secondarySectorName = holding.get("secondarySectorName", "")
                # 债券结束日期
                maturityDate = parse_date(holding.get("maturityDate", ""))
                # 债券行业
                superSectorName = holding.get("superSectorName", "")

                data_dic = {
                    "other_holding_isin": isin,
                    "other_country": country,
                    "other_securityName": securityName,
                    'other_primarySectorName': primarySectorName,
                    'other_secondarySectorName': secondarySectorName,
                    'other_weighting': weighting,
                    # 'other_ticker': ticker,
                    'other_holdingType': holdingType,
                    'other_maturityDate': maturityDate,
                    "other_sector": superSectorName
                }
                other_holding_list.append(data_dic)
            holdingList.extend(other_holding_list)

        fund_data_dic = {
            "cx_code": cx_code,
            'fund_type': fund_type,
            'baseCurrency': baseCurrency,
            'holding_date': holding_date,
            "holdingList": holdingList
        }
        print(fund_data_dic)
        fund_list.append(fund_data_dic)

        finished_data_dic = {
            "cx_code": cx_code,
            'holding_date': holding_date,
            "url": url
        }
        finished_list.append(finished_data_dic)
        url.update({'status': 1})

except Exception as e:
    print("e:",e)
    # 打开文件，写入数据
    with open("fund_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(fund_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 fund_list.txt')
    with open("fund_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(err_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 err_list.txt')
    with open("finished_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(finished_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 finished_list.txt')



try:
    excel_output(err_list, finished_list, fund_list)
except Exception as e:
    print("e:", e)
    # 打开文件，写入数据
    with open("fund_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(fund_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 fund_list.txt')
    with open("fund_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(err_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 err_list.txt')
    with open("finished_list.txt", 'w', encoding='utf-8') as file:
        file.write(str(finished_list))  # 每个基金名称后加一个换行符
        print(f'数据已保存到 finished_list.txt')


