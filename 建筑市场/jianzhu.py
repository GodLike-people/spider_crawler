import execjs
import requests

import subprocess
from functools import partial
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1717230562',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1717230562',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1717230562; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1717230562',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'accessToken': '',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
    'v': '231012',
}

params = {
    'pg': '2',
    'pgsz': '15',
    'total': '450',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
    params=params,
    cookies=cookies,
    headers=headers,)
print(response.text)

data=execjs.compile(open("jianzhu.js",'r',encoding='utf-8').read()).call("b",response.text)


print(data)