#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import DealJson
import sys
import os
import sys
import datetime


class NewFeed(object):
    def __init__(self, filepath, drive_path, new_json):
        self.path = filepath
        self.drive = drive_path
        self.new = new_json

    # 打印日志
    def make_print_to_file(self):
        '''
        path， it is a path for save your log about fuction print
        example:
        use  make_print_to_file()   and the   all the information of funtion print , will be write in to a log file
        :return:
        '''

        class Logger(object):
            def __init__(self, filename="Default.log", path="./"):
                self.terminal = sys.stdout
                self.log = open(os.path.join(path, filename), "a", encoding='utf8',)

            def write(self, message):
                self.terminal.write(message)
                self.log.write(message)

            def flush(self):
                pass

        fileName = datetime.datetime.now().strftime('day'+'%Y_%m_%d')
        sys.stdout = Logger(fileName + '.log')

        #############################################################
        # 这里输出之后的所有的输出的print 内容即将写入日志
        #############################################################
        print(fileName.center(60, '*'))


    # 浏览器利用xpath寻找元素
    def findelement(self, driver, xpath):
        global a
        try:
            a = ""
            a = driver.find_element_by_xpath(xpath).text
        except NoSuchElementException as e:
            print("错误信息", e.__class__.__name__, e)
        return a

    # 获取json文本某个字段，在浏览器找到对应字段的值，并写入文本中
    def getJson(self):
        line = 0
        chrome = 1
        json_list = []

        json = DealJson.DealJson(self.path)
        doc_id_list = json.get_doc_id()

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option_chrome = webdriver.Chrome(options=option)
        option_chrome.implicitly_wait(5)  # 设置隐式时间等待

        try:
            for doc_id in doc_id_list:
                if doc_id.isspace():
                    break
                if "vid" in doc_id:
                    option_chrome.get(self.drive +"video&docid=" + doc_id.split(":")[1])
                else:
                    option_chrome.get(self.drive +"mp&docid=" + doc_id)

                if chrome == 1:
                    try:
                        option_chrome.find_element_by_name("btn_smartlogin").click()
                    except Exception as e:
                        print("错误信息", e.__class__.__name__, e)

                for a in ["title", "mediaid", "url", "pic_url"]:
                    b = ""
                    if a == "title":
                        b = self.findelement(option_chrome, '//*[@fieldid="' + a + '"]/td[3]')
                    else:
                        b = self.findelement(option_chrome, '//*[@fieldid="' + a + '"]/td[3]/a')
                        if a == "mediaid":
                            b = b.split('(')[0].strip()
                    json_list.append(b)
                print(json_list)
                if len(json_list[0]):
                    json.get_line_json(json_list, self.new, line)
                else:
                    print(doc_id, "找不到内容")
                    json.write(self.new, line)
                json_list = []
                line = line + 1
                chrome = chrome + 1
        finally:
            option_chrome.close()


if __name__ == "__main__":
    file = "json_demo"
    driver = "http://rdata.mmsearch.oa.com/Pool/DetailInfo?domain="
    news_path = "json_demo_1"
    a = NewFeed(file, driver, news_path)
    a.make_print_to_file()
    a.getJson()
