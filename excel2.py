import pandas as pd

# 假设这是你的字典数据
data_dic = {
    "secId": "123333",
    "name": "Example Name",
    "cx_code": "CX456",
    "fundShareClassId": "FSC789",
    "assetType": "Asset Type A",
    "baseCurrencyId": "BC12",
    "countryId": "CTRY34",
    "newAssetType": "New Asset Type",
    "domicileCountryId": "DOMCTRY56"
}

# 将字典转换为DataFrame
df = pd.DataFrame([data_dic])

# 将DataFrame写入Excel文件
excel_filename = 'output.xlsx'
# 追加模式写入Excel文件，不写入索引
with pd.ExcelWriter(excel_filename, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
    # 如果Excel文件中没有工作表，则创建一个
    sheet_name = 'Sheet1'
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    # if writer.book.sheetnames == []:
    #     df.to_excel(writer, index=False)
    # else:
    #     # 如果工作表已存在，则将数据追加到工作表中
    #     df.to_excel(writer, index=False, startrow=len(writer.book.sheetbyname(writer.sheet_names[0]).iter_rows()))