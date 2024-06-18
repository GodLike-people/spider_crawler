
from flask import Flask,jsonify

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_cookie():
    option=webdriver.ChromeOptions()
    option.add_argument("headless")
    # 指定 ChromeDriver 的路径
    service = Service("D:\spider\爬虫案例\补环境\同花顺\chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=option)
    # 打开本地 HTML 文件
    driver.get("D:/spider/爬虫案例/补环境/同花顺/04-ths.html")
    return driver.execute_script("return window.aaa()")


#创建应用
app=Flask(__name__)

#配置路由 访问地址
@app.route("/s")
def hello():
    return jsonify(context={'v':get_cookie()})

if __name__ == '__main__':
    app.run()

