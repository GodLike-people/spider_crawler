import execjs
import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.birdreport.cn",
    "Referer": "https://www.birdreport.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "requestId": "55e81de24299544176489804694e544b",
    "^sec-ch-ua": "^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sign": "9c6fb37fefc8fe4b5d368d98387e48f0",
    "timestamp": "1718320588000"
}
data='page=1&limit=20&pointname=%E5%A3%B6%E7%93%B6%E5%B1%B1%E5%9B%BD%E5%AE%B6%E7%BA%A7%E8%87%AA%E7%84%B6%E4%BF%9D%E6%8A%A4%E5%8C%BA%E7%AE%A1%E7%90%86%E5%B1%80'
js_code=execjs.compile(open("观鸟网.js",encoding='utf-8').read())
all_data=js_code.call("beforeSend",data)
print(all_data)
headers["requestId"]=all_data['requestId']
headers["sign"]=all_data['sign']
headers["timestamp"]=all_data['timestamp']
print(headers)
url = "https://api.birdreport.cn/front/record/activity/search"
data = all_data["data"]
response = requests.post(url, headers=headers, params=data)
print(response.text)
parseData=js_code.call("parseData",response.json())
print(parseData)


