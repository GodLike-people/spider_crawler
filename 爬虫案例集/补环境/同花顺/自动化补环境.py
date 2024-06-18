from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 的路径
service = Service("D:\spider\爬虫案例\补环境\同花顺\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# 打开本地 HTML 文件
driver.get("D:/spider/爬虫案例/补环境/同花顺/04-ths.html")
print(driver.execute_script("return window.aaa()"))
# 等待 20 秒
# 关闭浏览器
driver.quit()

# 基本思路就是把js代码放到真实的浏览器环境中，执行js调用生成cookie的方法