import requests
import json


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "anti-content": "0aqAfxUeMwVEfK58XtqSRS-KIzX04WF8-V8XUyRhK_wETLTNwSg89cFn2y0X1LqHBlk4BfXEvJ6c90ghXqL-MF050B0D_Jp9w0UXsOpERXNKgMY8tExiKXErjU7XXb6XELYrMum28POEDJ9h2WgkB2ia6VzxGU6NKSxG102ve2E7sqA73p5MDt61e610kHTP1ER1UNV3ene1UGjY9mqA--MXXy0XD1eeUlc2YgLzlExrTmx8-VzX1y0Xv1E-UGu2YBkzvEqWETajUgjG99YnUQjTwVrMle4B6hEnFgER3VlTxV6MtbO9fhYS8FrtPadTkaU5bgOcJh7HjMKee_ds2wDLAO71RDF12D1eemMeM7M1AmMeMkd3hO-3RWI3R_SeREx7GjhzRJTa0R2ayQlqnGdycpX8XYXacp9yXGT7nWTJn04jXUTJnP4t26Tb22xzF0MDMf-eMdZTyzcDJ3veF3lKHL1SKB4wSZM7F1RADB47b54KEBAVDd4dX0XxsIZaOxgdNBxK49SnpajqphYwnCd8sYQ8gx2aiOUxnu6wqgSXYcvapyjlpcWdNg3KqVCnj7WyXZXYa9gsEPpyxtGXMsk7sQ_g7PnBZgshEF325MflTzz7UFstE-3-oghzk-2fFMMSO6MCMMvl7MRxzzw2wguwtcmPlBmM3yDs23vMZ65SvlArZpFSzl_LfZhkrh_uwoU2QFuS5K7B99VRhzz7LZsQ9C",
    "cache-control": "max-age=0",
    "content-type": "application/json",
    "origin": "https://seller.kuajingmaihuo.com",
    "priority": "u=1, i",
    "referer": "https://seller.kuajingmaihuo.com/login",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
cookies = {
    "api_uid": "CmkmRWZuhTKlwgBRKl4aAg==",
    "_nano_fp": "Xpmal0dalp9Jlpdan9_DjeR4b5IS7OfylnMsvYpX",
    "_bee": "2YtyVeyqBVte62EQDbH6sRGVws1tnamp",
    "_f77": "9668c6a2-9ab5-464d-8610-d6277e641462",
    "_a42": "c6cdd7d4-aad5-40ba-b8d0-7a09dd972d89",
    "rckk": "2YtyVeyqBVte62EQDbH6sRGVws1tnamp",
    "ru1k": "9668c6a2-9ab5-464d-8610-d6277e641462",
    "ru2k": "c6cdd7d4-aad5-40ba-b8d0-7a09dd972d89"
}
url = "https://seller.kuajingmaihuo.com/bg/quiet/api/mms/login"
data = {
    "loginName": "18952597444",
    "encryptPassword": "Xebw7jyaKGnX4FJ1LfDkuRYgk5B9REfOJGaXilwtyh3RyXOVNiq0cRolvs1N8xkO1T3NAZTszpHqyr0tmPVxWmnEJlf2fXD5O9Ck4N33Cm4KKzu+e/b6osQvtlj8x0NYuAUYGy7guM8ZR7U8Bslj4KztQbqvNBqG+RprJW8yPK4=",
    "keyVersion": "1"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)