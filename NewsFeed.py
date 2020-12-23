#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import DealJson
import Logger


class NewFeed(object):
    def __init__(self, filepath, drive_path, new_json):
        self.path = filepath
        self.drive = drive_path
        self.new = new_json

    def start(self):
        line = 0    # 写入json的行数
        chrome = 1  # 浏览器个数
        json = DealJson.DealJson(self.path)
        # 获取文本的 docid
        doc_id_list = json.get_doc_id()
        json_list = []
        # 静默模式启动
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option_chrome = webdriver.Chrome(options=option)
        option_chrome.implicitly_wait(5)  # 设置隐式时间等待
        media_id = ""
        title = ""
        url = ""
        pic_url = ""
        try:
            for doc_id in doc_id_list:
                if len(doc_id) == 0:
                    json.write(self.new, line)
                    line = line + 1
                    continue
                option_chrome.get(self.drive + str(doc_id))
                if chrome == 1:
                    option_chrome.find_element_by_name("btn_smartlogin").click()
                try:
                    title = option_chrome.find_element_by_xpath('//*[@fieldid="title"]/td[3]').text
                    if len(title) == 0:
                        print("title是空的", doc_id)
                except NoSuchElementException as e:
                    print('找不到标题', doc_id)
                try:
                    media_id_text = option_chrome.find_element_by_xpath('//*[@fieldid="mediaid"]/td[3]/a').text
                    media_id = media_id_text.split('(')[0].strip()  # 切割str，去除str两边空格
                except NoSuchElementException as e:
                    print('找不到来源', doc_id)
                try:
                    url = option_chrome.find_element_by_xpath('//*[@fieldid="url"]/td[3]/a').text
                except NoSuchElementException as e:
                    print('找不到url', doc_id)
                try:
                    pic_url = option_chrome.find_element_by_xpath('//*[@fieldid="pic_url"]/td[3]/a').text
                except NoSuchElementException as e:
                    print('找不到pic_url', doc_id)

                json_list.append(title)
                json_list.append(media_id)
                json_list.append(url)
                json_list.append(pic_url)

                if json_list:
                    json.get_line_json(json_list, self.new, line)
                    print(json_list)
                    json_list = []
                    line = line + 1
                else:
                    json.write(self.new, line)
                    line = line + 1
                chrome = chrome + 1

        except Exception as e:
            print('错误信息是：', e.__class__.__name__, e)
        finally:
            option_chrome.close()


if __name__ == "__main__":
    file = "json"
    drive = "http://rdata.mmsearch.oa.com/Pool/DetailInfo?domain=mp&docid="
    news_path = "json_1"
    a = NewFeed(file, drive, news_path)
    a.start()
