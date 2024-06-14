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
url = "https://api.birdreport.cn/front/record/activity/search"
data = {
    "BlS4WKnqaKWuG+m7JDMzUJ4oJKWS/vB0Qb4JUdROzKgNb2IRxlKBl+I+auRRRxPLM5RrdPe3slYjxiqM3GgWP46TxMKCt09Fbt4Cb1BN1IbRq2I2rOA8znNthxxwDitfJz7KjYLz3XiFsxUYX90XaemdPJlCmnWafubDgmLkRgdhYK7PcD74Ok/tHzaI5oxzEUdg04h0IUl7N9PgNN/pP94nMV8pOBQ9xUAVx6TQlPm1BAx0Nj5pe3i+d3xiX6waRZZku5kUdCsA9AjRjkZuhiV9a/wZ9nFEy0rdBrCPAzZxfGTgnc34NfAnpIqKYa8ZlTudTYkSJgPPpuHgrbsqpw": "="
}
response = requests.post(url, headers=headers, params=data)

print(response.text)

