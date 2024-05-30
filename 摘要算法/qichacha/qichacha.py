import execjs
import requests

cookies = {
    'qcc_did': '86923aef-fd77-4a53-a0ce-09a7ece226a5',
    'UM_distinctid': '18c29cf5879c07-06cdc5d3c8031-26001851-1fa400-18c29cf587a2123',
    'QCCSESSID': 'f41ba908a4fda8db1e6341cc9c',
    'tfstk': 'fXboOSawTg-S_LhLEZY7u4cSoTqAFYTBD93ppepU0KJjeY3RTeJhLKQJe_LrL2XHh4I8VHpntU_A22p8FefFBe2TBPU9Pf-B8Re9IVN_ieRUJpWHfMu6ReyTH3bNfSTCBv6dB8f4iBdpL0WeTIk2hBArz9Jy0xRM1eJFLePD0BdtYvRE8xJ2TjWZ8dbFlZPtYsDWBslduQxkK2pm-kVpZ3vNaK2aQZ4eqd5zj2y9jM0eKK_aHoffIgWJG94gne6fY9Rh3xypV6ScnQX8Iv9dP_QHe_qzFsYXEE7PjXuFiUvWxa-oE-vNPs76unUass7fe__c9XzeMOpVNa8375TkzL8DGwejzpjVYaKWRYy9V6ScnQYN4IiqbpYsRIPduDiB4ITMClFJxKuEQ9-TiSm_V3RXwRF0iDiB4IO8BSVmfvtyGQeO.',
    'CNZZDATA1254842228': '1686455543-1701508504-https%253A%252F%252Fwww.baidu.com%252F%7C1717079211',
}

json_data = {
    'searchKey': '小米',
    'pageIndex': 1,
    'pageSize': 20,
}
params = execjs.compile(open('qichacha.js', 'r').read()).call("get_params", json_data)
print(params)

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'qcc_did=86923aef-fd77-4a53-a0ce-09a7ece226a5; UM_distinctid=18c29cf5879c07-06cdc5d3c8031-26001851-1fa400-18c29cf587a2123; QCCSESSID=f41ba908a4fda8db1e6341cc9c; tfstk=fXboOSawTg-S_LhLEZY7u4cSoTqAFYTBD93ppepU0KJjeY3RTeJhLKQJe_LrL2XHh4I8VHpntU_A22p8FefFBe2TBPU9Pf-B8Re9IVN_ieRUJpWHfMu6ReyTH3bNfSTCBv6dB8f4iBdpL0WeTIk2hBArz9Jy0xRM1eJFLePD0BdtYvRE8xJ2TjWZ8dbFlZPtYsDWBslduQxkK2pm-kVpZ3vNaK2aQZ4eqd5zj2y9jM0eKK_aHoffIgWJG94gne6fY9Rh3xypV6ScnQX8Iv9dP_QHe_qzFsYXEE7PjXuFiUvWxa-oE-vNPs76unUass7fe__c9XzeMOpVNa8375TkzL8DGwejzpjVYaKWRYy9V6ScnQYN4IiqbpYsRIPduDiB4ITMClFJxKuEQ9-TiSm_V3RXwRF0iDiB4IO8BSVmfvtyGQeO.; CNZZDATA1254842228=1686455543-1701508504-https%253A%252F%252Fwww.baidu.com%252F%7C1717079211',
    # 'da4728817277230574d7': '3af13cd7482a6a7c35ee2669208cec12358bebe1f57a5d0ff7b9babd0d4ce7f43e28ea89431889db38e5fdd11426b1e110a30975c543c75637e0622c099516fe',
    'origin': 'https://www.qcc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.qcc.com/web/search?key=%E5%B0%8F%E7%B1%B3',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-pid': '57d94eb35137dbaec407200d6b9ed4ae',
    'x-requested-with': 'XMLHttpRequest',
}
headers[params[0]] = params[1]
print(headers)

response = requests.post('https://www.qcc.com/api/search/searchMulti', cookies=cookies, headers=headers, json=json_data)

print(response.text)
