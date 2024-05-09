#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :vess.py
# @Time     :2024/5/816:14
# @Author   :aczhang
from datetime import datetime


import pandas as pd

fund_list=[
{'cx_code': 'F00000OMYL', 'fund_type': 'FIXEDINCOME', 'baseCurrency': 'CAD', 'holding_date': '20240331', 'holdingList': [{'bond_holding_isin': 'US88632QAE35', 'bond_country': 'United States', 'bond_securityName': 'Tibco Software Inc', 'bond_stockRating': None, 'bond_weighting': 1.17797, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20290331', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Technology'}, {'bond_holding_isin': 'US44332PAJ03', 'bond_country': 'United States', 'bond_securityName': 'HUB International Ltd.', 'bond_stockRating': None, 'bond_weighting': 1.13898, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20320131', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Financial Services'}, {'bond_holding_isin': 'US44332PAH47', 'bond_country': 'United States', 'bond_securityName': 'HUB International Ltd.', 'bond_stockRating': None, 'bond_weighting': 0.97534, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20300615', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Financial Services'}, {'bond_holding_isin': 'US57763RAB33', 'bond_country': 'United States', 'bond_securityName': 'Mauser Packaging Solutions Holding Co.', 'bond_stockRating': None, 'bond_weighting': 0.8525, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20260815', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Consumer Cyclical'}, {'bond_holding_isin': 'US29103CAA62', 'bond_country': 'United States', 'bond_securityName': 'EMRLD Borrower LP / Emerald Co-Issuer Inc.', 'bond_stockRating': None, 'bond_weighting': 0.84361, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20301215', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Unspecified'}, {'bond_holding_isin': 'US90279XAA00', 'bond_country': 'United States', 'bond_securityName': 'UKG Inc.', 'bond_stockRating': None, 'bond_weighting': 0.82768, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20310201', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Technology'}, {'bond_holding_isin': 'US98919VAA35', 'bond_country': 'United States', 'bond_securityName': 'Zayo Group Holdings Inc', 'bond_stockRating': None, 'bond_weighting': 0.82477, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20270301', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Communication Services'}, {'bond_holding_isin': 'US14366RAA77', 'bond_country': 'United States', 'bond_securityName': 'Carnival Holdings Bermuda Ltd.', 'bond_stockRating': None, 'bond_weighting': 0.7936, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20280501', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Industrials'}, {'bond_holding_isin': 'US92535WAA80', 'bond_country': 'United States', 'bond_securityName': 'Verscend Escrow Corp', 'bond_stockRating': None, 'bond_weighting': 0.72586, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20260815', 'bond_primarySectorName': 'Corporate Bond', 'bond_secondarySectorName': 'Financial Services'}, {'other_holding_isin': 'IE00B4PY7Y77', 'other_country': 'Ireland', 'other_securityName': 'iShares $ High Yld Corp Bd ETF USD Dist', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 2.38744, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}]}
,
{'cx_code': 'F00000PLRY', 'fund_type': 'ALLOCATION', 'baseCurrency': 'AUD', 'holding_date': '20240331', 'holdingList': [{'equity_holding_isin': 'TW0002330008', 'equity_country': 'Taiwan', 'equity_securityName': 'Taiwan Semiconductor Manufacturing Co Ltd', 'equity_stockRating': '4', 'equity_weighting': 0.53077, 'equity_sector': 'Technology', 'equity_ticker': '2330', 'equity_holdingType': 'Equity'}, {'bond_holding_isin': None, 'bond_country': None, 'bond_securityName': 'Us 5Yr Note Jun 24', 'bond_stockRating': None, 'bond_weighting': 12.68679, 'bond_holdingType': 'Bond', 'bond_maturityDate': None, 'bond_primarySectorName': 'governmentRelated', 'bond_secondarySectorName': 'Treasury Future'}, {'bond_holding_isin': 'DE000C75XMU8', 'bond_country': 'Germany', 'bond_securityName': 'Euro Bund Future June 24', 'bond_stockRating': None, 'bond_weighting': 6.18156, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20240606', 'bond_primarySectorName': 'governmentRelated', 'bond_secondarySectorName': 'Treasury Future'}, {'bond_holding_isin': None, 'bond_country': None, 'bond_securityName': 'Us 10Yr Note Jun 24', 'bond_stockRating': None, 'bond_weighting': 4.09639, 'bond_holdingType': 'Bond', 'bond_maturityDate': None, 'bond_primarySectorName': 'governmentRelated', 'bond_secondarySectorName': 'Treasury Future'}, {'bond_holding_isin': 'US912828H458', 'bond_country': 'United States', 'bond_securityName': 'United States Treasury Notes', 'bond_stockRating': None, 'bond_weighting': 0.50082, 'bond_holdingType': 'Bond', 'bond_maturityDate': '20250115', 'bond_primarySectorName': 'government', 'bond_secondarySectorName': 'inflationProtected'}, {'other_holding_isin': 'IE00BKM4H312', 'other_country': 'Ireland', 'other_securityName': 'iShares MSCI USAQualDiv ESG ETF USD Dis', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 3.83498, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}, {'other_holding_isin': 'IE00B4PY7Y77', 'other_country': 'Ireland', 'other_securityName': 'iShares $ High Yld Corp Bd ETF USD Dist', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 2.07133, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}, {'other_holding_isin': 'IE00BZ6V7883', 'other_country': 'Ireland', 'other_securityName': 'iShares US Mortg Backed Secs ETF USD Dis', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 1.13396, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}, {'other_holding_isin': 'LU1376384019', 'other_country': 'Luxembourg', 'other_securityName': 'BGF US Dollar High Yield Bd X6 USD', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 0.92414, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}, {'other_holding_isin': 'IE0031442068', 'other_country': 'Ireland', 'other_securityName': 'iShares Core S&P 500 ETF USD Dist', 'other_primarySectorName': None, 'other_secondarySectorName': None, 'other_weighting': 0.75596, 'other_holdingType': 'Other', 'other_maturityDate': None, 'other_sector': None}]}


]
def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"读取Excel文件时发生错误：{e}")
        return None

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

excel_output_append(fund_list,'2029holdings_2.xlsx')

# df = read_excel_file('2029holdings_2.xlsx')
# print(df)