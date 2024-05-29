import execjs
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'origin': 'https://www.mytokencap.com',
    'priority': 'u=1, i',
    'referer': 'https://www.mytokencap.com/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

param=execjs.compile(open("mytoken.js",'r').read()).call("get_params")
print(param)
params = {
    'pages': '2,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'en_US',
    'legal_currency': 'USD',
    'timestamp': param[0],
    'code': param[1],
    'platform': 'web_pc',
    'v': '0.1.0',
    'international': '1',
}

response = requests.get('https://api.mytokenapi.com/ticker/currencyranklist', params=params, headers=headers)
print(response.text)