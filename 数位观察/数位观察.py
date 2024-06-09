import execjs
import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.swguancha.com",
    "Referer": "https://www.swguancha.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "deviceType": "1",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://app.swguancha.com/client/v1/cPublic/consumer/property/rankingList/multi"
data = {
    "propertyCode": [
        "DISTRICT_PROP_GJ024_DQSCZZ",
        "DISTRICT_PROP_GJ025_RJDQSCZZ",
        "DISTRICT_PROP_GJ026_DQSCZZZCL",
        "DISTRICT_PROP_GJ027_DYCYZDQSCZZDBZ",
        "DISTRICT_PROP_GJ028_DECYZDQSCZZDBZ",
        "DISTRICT_PROP_GJ029_DSCYZDQSCZZDBZ"
    ],
    "dimensionTime": "2023",
    "orderFieldList": {
        "field": "DISTRICT_PROP_GJ024_DQSCZZ",
        "rule": "desc"
    },
    "propertyType": "GDP",
    "typeCode": "gdp",
    "current": 2,
    "size": 10,
    "levelType": 2,
    "regionCode": ""
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)

js_code=execjs.compile(open("数位观察.js",encoding='utf-8').read())
data=js_code.call("get_decrypt",response.text)
print(data)