import datetime

from time import sleep

import readxls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


start = datetime.datetime.now()
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器

driver.implicitly_wait(5)  # 设置隐式时间等待

driver.get("https://weixin.oa.com/")

driver.find_element_by_name("btn_smartlogin").click()

driver.get("https://weixin.oa.com/itilwebmmtools/view/click_stream")

driver.find_element_by_id("reason").send_keys("测试")
driver.find_element_by_class_name("btn-container").click()

WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located
                                   ((By.CLASS_NAME,"col-md-2")))

filepath = "E://PyCharm-Project//_tmp_robertzhan.xls"
data = readxls.ReadExcel(filepath,"account")
alias = []
for i in data.username():
    username = driver.find_element_by_class_name("search-input")
    username.send_keys(i)
    button = driver.find_element_by_class_name("search-btn")
    button.click()
    sleep(6)
    try:
        Alia = driver.find_element_by_xpath('// *[@class="basic-info-table"]/tbody/tr/td[4]').text
    except:
        Alia = "找不到"
        print(i, Alia)
    if Alia is None:
        print(i, data.password(i))
    alias.append(Alia)
    username.clear()
print(alias)
data.writer(alias)
driver.close()