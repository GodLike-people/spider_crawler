### 如何运行？
python环境装好，下载js文件&py文件，运行py文件节课

### 七麦逆向知识点

简单混淆，webpack，扣js，参数定位，js异步跟栈，interceptors拦截器

注意：

遇到requests返回数据是unicode编码，可以使用json模块之间转换
import json
import requests
response = requests.get('你的URL')
json_str = response.text  
解析JSON字符串并自动处理Unicode编码
data = json.loads(json_str)print(data['msg'])  
或者直接
json_str = response.json()  
