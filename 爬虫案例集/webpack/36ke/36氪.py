import requests
import json

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://36kr.com",
    "Referer": "https://36kr.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_1684191ccae0314c6254306a8333d090": "1718438486",
    "Hm_lpvt_1684191ccae0314c6254306a8333d090": "1718438486",
    "Hm_lvt_713123c60a0e86982326bae1a51083e1": "1718438486",
    "Hm_lpvt_713123c60a0e86982326bae1a51083e1": "1718438486",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221895879c9341142-09705d993d966-26031d51-2073600-1895879c93511c3%22%2C%22%24device_id%22%3A%221895879c9341142-09705d993d966-26031d51-2073600-1895879c93511c3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
    "aliyungf_tc": "3487a2da46be4de95c43c706f5600ea4b6106ab498aac8a2d8120c08041b287d",
    "acw_tc": "ac11000117184384903293629e25b6b7e1b56c4929caebfb9847d565d862de",
    "tfstk": "fRjJoh0XtSVk5M4hVTacKzcRMQy0SgByq_WsxBAoRsCvddxkK9NP9MdXVe7ktQApv95Tn5qgjTWyYeNgsl2B8oUJb4OIPXmXGp__DjTQjTWrhCPlXpriJMI7DJdCOUTXcdOjR2iCOjOXgpJINpi7HtO2dHiWdLZXcd9sRL9SNsNpGYOnvwQZ8O1z_m0n-ipbTpW-jqOFbLLJ1Ts-ADwweUd1FIFi4h5Bl98dYvopJT_NTd1SN5YPdZCveHEmPh6AR1pVVlcJ3aXfII6tLDWy2pL6AEHIAtKyGFsXflGv3Z6lRg5-pD9PqGYp_EeIYexfjF_1wvyNh39CTFS3_0R5dOSNShEmPh6AR1Qd4BSGXFLIsCpnP-ex828Wno8qAqg8lmuHHC28v2ueu-Jvs-ex828W3Kdge73E8EyV."
}
url = "https://gateway.36kr.com/api/mus/login/byMobilePassword"
data = {
    "krtoken": "",
    "partner_id": "web",
    "timestamp": 1718438797074,
    "param": {
        "countryCode": "86",
        "mobileNo": "TJ44O8yQRO8oE4g1y+ZMGC5l+OFtA0o7otJTO8sEm5uagek7+uuSzfeCv8JJ7G4MizLmeiK9VEcltyhFXG09ggbtFMk+/wYxY1dQg8mYyVI05s3asLkE+mum6q7FdHkPEEY6Zq+kXomfRxeyg+6ALrqdVWPXFGyQIhhHzxFuZTU=",
        "password": "OGAq8HLGfGYSXE+5m5rckMVd2Avmc3i1nlhqbjHbzBRwNPunPQ6YQZJv2mjcl/vDiqOO+dqNZe5QpGsanbuQk/CV4/OZMQAmzK2jG2ZvB4m1N5oN3sYSZBU68OAwt1ITYFNB0RpQ4QhJJSj5BbpGPuE2kr4dDKeszRAa/m6Mbus="
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)