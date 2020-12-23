import datetime

from time import sleep

import readxls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WeiXin (object):
    def __init__(self, filepath, sheet):
        self.filepath = filepath
        self.sheet = sheet

    def search_name(self):
        driver = webdriver.Chrome()
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(5)  # 设置隐式时间等待
        driver.get("https://weixin.oa.com/")
        driver.find_element_by_name("btn_smartlogin").click()
        driver.get("https://weixin.oa.com/itilwebmmtools/view/click_stream")
        driver.find_element_by_id("reason").send_keys("测试")
        driver.find_element_by_class_name("btn-container").click()
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "col-md-2")))
        data = readxls.ReadExcel(self.filepath, self.sheet)
        alias = []
        uin_list = []

        for i in data.username():
            username = driver.find_element_by_class_name("search-input")
            username.send_keys(i)
            button = driver.find_element_by_class_name("search-btn")
            button.click()
            sleep(3)
            try:
                alia = driver.find_element_by_xpath('// *[@class="basic-info-table"]/tbody/tr/td[4]').text
                uin_name = driver.find_element_by_xpath('// *[@class="basic-info-table"]/tbody/tr[2]/td[4]').text
                alias.append(alia)
                uin_list.append(uin_name)
                username.clear()
            except :
                alia = "找不到"
                uin_name = "找不到"
        data.writer(alias, 5)
        data.writer(uin_list, 6)
        driver.close()


if __name__ == "__main__":
    filepath = "E://PyCharm-Project//_tmp_robertzhan.xls"
    name = WeiXin(filepath, "account")
    name.search_name()
