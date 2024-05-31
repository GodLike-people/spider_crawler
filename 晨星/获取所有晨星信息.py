#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :获取所有晨星信息.py
# @Time     :2024/5/714:22
# @Author   :aczhang
import pandas as pd
import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'origin': 'https://www.morningstar.hk',
    'priority': 'u=1, i',
    'referer': 'https://www.morningstar.hk/hk/screener/fund.aspx',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
}

params = {
    'page': '1',
    #修改下载额度
    'pageSize': '20000',
    'sortOrder': 'LegalName asc',
    'outputType': 'json',
    'version': '1',
    'languageId': 'en-HK',
    'currencyId': 'HKD',
    'universeIds': 'FOHKG$$ALL',
    'securityDataPoints': 'SecId|Name|PriceCurrency|TenforeId|LegalName|ClosePrice|Yield_M12|CategoryName|Medalist_RatingNumber|StarRatingM255|SustainabilityRank|GBRReturnD1|GBRReturnW1|GBRReturnM1|GBRReturnM3|GBRReturnM6|GBRReturnM0|GBRReturnM12|GBRReturnM36|GBRReturnM60|GBRReturnM120|MaxFrontEndLoad|OngoingCharge|ManagerTenure|MaxDeferredLoad|InitialPurchase|FundTNAV|EquityStyleBox|BondStyleBox|AverageMarketCapital|AverageCreditQualityCode|EffectiveDuration|MorningstarRiskM255|AlphaM36|BetaM36|R2M36|StandardDeviationM36|SharpeM36|TrackRecordExtension',
    'filters': '',
    'term': '',
    'subUniverseId': '',
}

response = requests.get(
    'https://tools.morningstar.co.uk/api/rest.svc/roq2rh8blz/security/screener',
    params=params,
    headers=headers,
)

rows_list=json.loads(response.text).get("rows")
print(rows_list)
all_list=[]
for row in rows_list:
    LegalName=row.get("LegalName")
    PriceCurrency=row.get("PriceCurrency")
    SecId=row.get("SecId")
    TenforeId=row.get("TenforeId")
    data_dic={
        'LegalName':LegalName,
        'PriceCurrency':PriceCurrency,
        'SecId':SecId,
        'TenforeId':TenforeId
    }
    all_list.append(data_dic)

df = pd.DataFrame(all_list)
# 将 DataFrame 写入 Excel 文件
df.to_excel('晨星id汇总.xlsx', index=False)




