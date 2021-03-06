#!/usr/bin/python
# -*- coding: UTF-8 -*-
import demjson
from selenium import webdriver


class Test(object):

    # 判断起始字符和切割
    def textstart(self, text):
        if text.startswith("{"):
            print("{")
        else:
            text = text.split("{", 1)[1]
            print(type(text))

    # 文本写入
    def write_file(self, filepath, newline):
        with open(filepath, "a", encoding='utf-8') as f:
            f.writelines(newline+"\n")
            f.close()

    # 静默启动浏览器
    def demjson(self):
        with open(self.path) as f:
            f = f.readline()
            print("解码", demjson.decode(f))
            print("编码", demjson.encode(f))
        # 静默模式启动
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option_chrome = webdriver.Chrome(options=option)
        option_chrome.implicitly_wait(5)  # 设置隐式时间等待
        return option_chrome

    # 普通启动浏览器
    def start(self):
        option_chrome = webdriver.Chrome()
        # driver.maximize_window()  # 最大化浏览器
        option_chrome.implicitly_wait(5)  # 设置隐式时间等待
        return option_chrome

    # 浏览器启动新窗口
    def newchromewindow(self, option_chrome, path):
        js = 'window.open("' + path + '");'
        option_chrome.execute_script(js)


if __name__ == "__main__":
    #data = Test()
    a = ["1"]
    if len(a[0]):
        print(a)

