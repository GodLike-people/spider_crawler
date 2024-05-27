### 如何运行？
python环境装好，下载js文件&py文件，运行py文件节课

### 七麦逆向知识点

简单混淆，webpack，扣js，参数定位，js异步跟栈，interceptors拦截器

### 逆向回顾 
经过分析，发现请求加密为get请求里的analysis参数，analysis搜索无果，遂使用XHR断点，上下寻找，直到找到加密位置所在（当前执行的不是加密数据，执行的下一步则成加密数据）。

本次加密数据是在循环interceptors异步请求中，遂需要一步步的调试，找到详细加密位置。

找到之后，开始分析js代码，有些混淆，但主要是数据都是写死。（注意：有些方法请求返回的都是固定值，不需要再去逐步寻找方法，写固定值即可）

如此也就衍生出，在扣代码的一些技巧：

1 找到加密位置，先分析结构（三元运算符、逻辑表达式等）

2 对切分的每个模块进行查看，看是否为固定值 

3 再细看数据，哪些是真正需要扣出的代码


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

可以解决，返回数据为unicode编码的问题
