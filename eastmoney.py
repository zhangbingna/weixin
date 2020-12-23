

from selenium import webdriver

driver = webdriver.Chrome()
#drive.maximize_window()  # 最大化浏览器
#drive.implicitly_wait(5)  # 设置隐式时间等待
driver.get("http://fund.eastmoney.com/daogou/")

#print()