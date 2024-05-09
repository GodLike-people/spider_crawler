#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :测试.py
# @Time     :2024/5/715:02
# @Author   :aczhang
import random
import re
import requests

def get_mass_token():
    cx_code_list = ['0P00002C42', '0P00002C21', '0P0001H1ZQ', '0P0001H1ZG', '0P0001I2RK', '0P0001I2C4', '0P0001I2RJ',
                    '0P0001I2C3', '0P0001I3WN', '0P0001I3WL', '0P0001I3WO', '0P0001I3WM', '0P0001IQSA', '0P00006SOO',
                    '0P0001IGUS', '0P0001IH6G', '0P00006SON', '0P0001IMI6', '0P0001IMNI', '0P0001J6MJ', '0P0001J6MH',
                    '0P0001J6MM', '0P0001J6MK', '0P0001J6ME', '0P0001J6MC', '0P0001K9T2', '0P0001K9DO', '0P0001K57J',
                    '0P0001K2V8', '0P0001K57I', '0P0001KFZU', '0P0001KFUA', '0P0001KIKG', '0P0001KIKH', '0P0001KIKI',
                    '0P0001KIKJ', '0P0001KQJ7', '0P0001KQJ9', '0P0001LX8A', '0P0001LX8B', '0P0001M4LA', '0P0001M4JT',
                    '0P0001M4L9', '0P0001M4LG', '0P0001M4JS', '0P0001M4LH', '0P0001MIGF', '0P0001MKPP', '0P0001MKPJ',
                    '0P0001P25B', '0P0001P25A', '0P0001OWSY', '0P0001MZW7', '0P0001MZW8', '0P0001MZW6', '0P0001OE1M',
                    '0P0001OE1N', '0P0001MZWD', '0P0001N4PY']
    cx_code = random.choice(cx_code_list)
    url=f'https://www.morningstar.hk/hk/report/fund/performance.aspx?t={cx_code}&fundservcode=&lang=en-HK'
    res=requests.get(url)
    # 使用正则表达式提取maas_token后面的数据
    match = re.search(r'maas_token="([^"]+)"', res.text)
    if match:
        maas_token = match.group(1)
        # print(f"maas_token: {maas_token}")
        return maas_token

maas_token = get_mass_token()

def generate_random_string():
    result = ""
    for n in range(1, 33):
        result += format(random.randint(0, 15), 'x')
        if n in [8, 12, 16, 20]:
            result += "-"
    return result

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'authorization':'Bearer '+maas_token,
    #  'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EY3hOemRHTnpGRFJrSTRPRGswTmtaRU1FSkdOekl5TXpORFJrUTROemd6TWtOR016bEdOdyJ9.eyJodHRwczovL21vcm5pbmdzdGFyLmNvbS9tc3Rhcl9pZCI6Ijc2NjU2NkFELTkxMjEtNDJDMS05RjM2LTkwREM1RkNENUUxQyIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL3Bhc3N3b3JkQ2hhbmdlUmVxdWlyZWQiOmZhbHNlLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9lbWFpbCI6Imo2M2s4OTVuanBhOG1ubXE0cDJqbXN0dGNoOTBzYWhiQG1hYXMtbXN0YXIuY29tIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcm9sZSI6WyJFQy5TZXJ2aWNlLkNvbmZpZ3VyYXRpb24iLCJFQy5TZXJ2aWNlLkhvc3RpbmciLCJFQ1VTLkFQSS5BdXRvY29tcGxldGUiLCJFQ1VTLkFQSS5TY3JlZW5lciIsIkVDVVMuQVBJLlNlY3VyaXRpZXMiLCJQQUFQSVYxLlhyYXkiLCJWZWxvVUkuQWxsb3dBY2Nlc3MiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vY29tcGFueV9pZCI6IjI4MmNjODY1LTM1MDUtNGUyMC04ZDI0LTg0YTQzOGIyMTkyNCIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2ludGVybmFsX2NvbXBhbnlfaWQiOiJDbGllbnQwIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vZGF0YV9yb2xlIjpbIkVDVVMuRGF0YS5VUy5PcGVuRW5kRnVuZHMiLCJRUy5NYXJrZXRzIiwiUVMuUHVsbHFzIiwiU0FMLlNlcnZpY2UiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vbGVnYWN5X2NvbXBhbnlfaWQiOiIyNGJmMGE4NS0zMjcxLTRiMWItYWIxZS0wZTlmZDE4ODE4YmQiLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS91aW1fcm9sZXMiOiJFQU1TLE1VX01FTUJFUl8xXzEiLCJpc3MiOiJodHRwczovL2xvZ2luLXByb2QubW9ybmluZ3N0YXIuY29tLyIsInN1YiI6ImF1dGgwfDc2NjU2NkFELTkxMjEtNDJDMS05RjM2LTkwREM1RkNENUUxQyIsImF1ZCI6WyJodHRwczovL2F1dGgwLWF3c3Byb2QubW9ybmluZ3N0YXIuY29tL21hYXMiLCJodHRwczovL3VpbS1wcm9kLm1vcm5pbmdzdGFyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTUwNjY4MjgsImV4cCI6MTcxNTA3MDQyOCwic2NvcGUiOiJvcGVuaWQiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6ImlRa1d4b2FwSjlQeGw4Y0daTHlhWFpzYlhWNzlnNjRtIn0.SVrCFAbPR51sjiLFtwjimRkwHNNkkaHYq3DGEytvAd0LQ5So6ppVM_t9J_romrxLZMROO-PHZfD9rE6VJtJA8IHQqvfVJW853ZHls-v3Dft57heASAHBxC52goVIEe_skdgDgptNb4_SzXs9D_qXBQbVdJ758aHrdjorboA05uRDZqzTKA3DNj6MxBnjf-fhTh_3eNUoR2lSb46NHWNJzZ-9NJyosv6Y-b_1QwF_6Ty_hYNDBH5ziJRySeBWa9kiu8z7uLg-40v7qIncL34DaYKcyLJ8nvUoym0S_j1OJnzH9Gn67TM7katDClyqDjMt-nIiFo9lP2GpP65kQaMmSg',
    'credentials': 'omit',
    'origin': 'https://www.morningstar.hk',
    'priority': 'u=1, i',
    'referer': 'https://www.morningstar.hk/hk/report/fund/portfolio.aspx?t=0P00001B6G&lang=en-HK',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'x-api-realtime-e': 'eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.jidbnhWUJvWMvD2omPxv9L_-iiW424c89SMUexsXDrY3VE6CfIU1g6cRPZ-DToeSbtFEvMPV4DoNlOtzUJ63Ryja23rtjlMsrpV-nLpUUpjcZp7ZL0YjGQNbsq1a-vAwf7GBOk6lnsOWycXB0mKaHMXfHpgwAsRcfGK1QpIb27U.da0qHJBnRmc0_EOq.1fXioE66EIItzsggPK3b4HNypNp1Ltva84HWRNmxwBPsUo5kvUXaYDuFjLHT2K39RsoMqZzERuQMfrP8fYoqTfkBmg-xD5sQbqHYeKgvuqMdOlkRVx4y16ft1RiliknyWNGxTd_5KXZrkDadGR7gHQyC775iNEBi0bI9F_JXu3t7_8uBMHNOYlIeRHm2Dqmz17ukL_zoGOX74_KiaYkBL5RamA.7wz-dbBZR15KCDRanQrHPg',
    'x-api-requestid': generate_random_string(),
    'x-sal-contenttype': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU=',
}

response = requests.get(
    'https://www.us-api.morningstar.com/sal/sal-service/fund/securityMetaData/0P0001HDB4',
    headers=headers,
)
print(response.text)

