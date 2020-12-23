#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time, logging, datetime
from selenium.webdriver.support.select import Select
from time import sleep

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

start = datetime.datetime.now()
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器

driver.implicitly_wait(5)  # 设置隐式时间等待

driver.get("http://9.134.55.214:8881/feedback")

js = "document.getElementById('start_date').removeAttribute('readonly')"  # 去掉前端的readonly
driver.execute_script(js)
driver.find_element_by_id("start_date").send_keys(time.strftime("2020-04-06"))  # 输入日期
# driver.find_element_by_id("start_date").send_keys(time.strftime("%Y%m%d")) # 获取当前时间并格式化
js = "document.getElementById('end_date').removeAttribute('readonly')" # 去掉前端的readonly
driver.execute_script(js)
driver.find_element_by_id("end_date").send_keys(time.strftime("2020-04-09"))  # 获取当前日期time.strftime("%Y/%m/%d")
# driver.find_element_by_id("end_date").send_keys(time.strftime("2019-06-13")) # 获取当前日期time.strftime("%Y/%m/%d")

driver.find_element_by_id("filter_feeds_button").click()
driver.find_element_by_name("feedTable_length").send_keys("100")

WebDriverWait(driver, 25, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                   '// *[ @ id = "feedTable"] / tbody / tr[1] / td[8] / div / button')))

# 获取页数

a = driver.find_element_by_xpath('//*[@id="feedTable_paginate"]/span/a[last()]').text

x = 0
y = 0
exit_flag = True
'''
dict = {
    "privacy": ["隐私", "私隐", "不想别人看", "隱私", "稳私", "泄露", "瘾私"],
    "turnoff" : ["关闭", "关掉", "不想要这个功能"],
    # 内容
    "content_quality": ["质量", "垃圾", "文理不通", "乱七八糟","广告"],
    "swindle": ["诈骗","传销","古币", "钱币"],
    "Links_hijack" : ["链接"],
    "stock": ["股票"],
    "sex": ["色情", "低俗"],
    "false": ["虚假", "骗人"],
    "religion": ["穆斯林", "基督"],
    "old_news" :["新闻旧","不及时"],
    "title": ["标题党", "文不对题", "张冠李戴", "标题与内容不符", "雷人标题"],
    # 视频
    "video_play": ["视频打不开", "不能播放", "视频异常", "无法播放"],
    "video_blank" : ["视频黑屏"],
    "video_quality" : ["视频质量差"],
    "video_incomplete" : ["视频内容不完整"],
    "video_block": ["视频无响应", "视频卡"],
    # 功能
    "picture": ["图片打不开", "图片加载不了"],
    "doc": ["文章打不开"],
    "not_open": ["看一看打不开"],
    "white_screen": ["白屏", "什么都不显示", "不显示内容"],
    "blank_screen": ["黑屏"],
    "gibberish": ["文字乱码"],
    "crash" : ["闪退", "重启"],
    "newPoint": ["红点消不了","有消息盒子"],
    "feeds": ["刷不出来"],
    # 入口
    "discover" : ["发现页管理", "发现管理页"],
    # 样式
    "word": ["字体"],
    # 其他
    "memory": ["占内存", "占空间"],
    "addNewFunction": ["全选", "浏览历史", "瀏覽歷史", "一键屏蔽", "建议", "希望"],

}
content = {
    "privacy": ["担心泄露隐私"],
    "turnoff" : ["想关闭看一看"],
    # 内容
    "content_quality": ["内容质量差"],
    "swindle": ["传销诈骗"],
    "Links_hijack" : ["链接劫持"],
    "stock": ["推股荐股"],
    "sex": ["色情低俗"],
    "false": ["虚假信息"],
    "religion": ["宗教反馈"],
    "old_news": ["新闻老旧/不及时"],
    "title": ["标题党"],
    # 视频
    "video_play": ["视频无法播放"],
    "video_blank" : ["视频黑屏"],
    "video_quality" : ["视频质量差"],
    "video_incomplete" : ["视频内容不完整"],
    "video_block": ["视频卡顿"],
    # 功能
    "picture": ["图片加载不出"],
    "doc": ["文章打不开"],
    "not_open": ["看一看打不开"],
    "white_screen": ["看一看白屏"],
    "blank_screen": ["看一看黑屏"],
    "crash": ["看一看闪退"],
    "gibberish": ["看一看文字乱码"],
    "newPoint": ["红点消不了"],
    "feeds": ["刷新不出feeds"],
    # 入口
    "discover" : ["欧盟用户找不到入口"],
    # 样式
    "word": ["字体反馈"],
    # 其他
    "memory": ["认为看一看占内存"],
    "addNewFunction": ["新增功能反馈"],
}
entry = ["找不到入口", "没有看一看"]
for j in range(int(a)):
    num = 0
    num2 = 0
    for i in range(100):
        try:
            bianji = driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[" + str(i + 1) + "]/following::button[1]")
        except NoSuchElementException:
            break
        con = driver.find_element_by_xpath('// *[ @ id = "feedTable"]/tbody/tr[' + str(i + 1) + '] / td[6]')
        osCon = driver.find_element_by_xpath("//*[ @ id = 'feedTable']/tbody/tr[" + str(i + 1) + "]/td[3]")

        try:
            for k, v in dict.items():
                for a in v:
                    if a in con.text:
                        print(con.text)
                        print(content[k])
                        bianji.click()
                        s = driver.find_element_by_id("mySelect")
                        Select(s).select_by_value(str(content[k]))
                        #driver.find_element_by_id("mySelect").click()

                        #driver.find_element_by_id("mySelect").send_keys(str(content[k]))
                        bianji.click()
                        num2 = num2 + 1
                        raise KeyError

            for a in entry:
                if a in con.text:
                    print(con.text)
                    if osCon.text[0] == "a":
                        os = osCon.text.split("-")
                        # logging.info("android os: " + str(os))
                        if int(os[1]) >= 27:
                            bianji.click()
                            driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                            bianji.click()
                            print("['欧盟用户找不到入口1']")
                            num2 = num2 + 1
                        else:
                            bianji.click()
                            driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                            bianji.click()
                            print("['看一看入口找不到1']")
                            num2 = num2 + 1
                    elif osCon.text[0] == "i":
                        if osCon.text[1] == "O":
                            os = osCon.text.split(" ")
                            try:
                                osVersion = os[1].split(".")[0]
                                # logging.info("ios os: " + str(os) + ", isVersion: " + str(osVersion))
                            except IndexError:
                                continue
                            if int(osVersion) >= 12:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                bianji.click()
                                print("['欧盟用户找不到入口2']")
                                num2 = num2 + 1
                            else:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                bianji.click()
                                print("['看一看入口找不到2']")
                                num2 = num2 + 1
                        elif osCon.text[1] == "P":
                            os = osCon.text.split(" ")

                            try:
                                osVersion = os[2].split(".")[0]
                            except IndexError:
                                raise KeyError
                            # logging.info("ios os: " + str(os) + ", isVersion: " + str(osVersion))
                            if int(osVersion) >= 12:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                bianji.click()
                                print("['欧盟用户找不到入口3']")
                                num2 = num2 + 1
                            else:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                bianji.click()
                                print("['看一看入口找不到3']")
                                num2 = num2 + 1
                    raise KeyError

        except KeyError:
            continue
        num = num + 1
    print("---------------------------------------")
    print("第%d页" % (j + 1))
    print("编辑%d条" % num2)
    print("未编辑%d条" % num)
    print("---------------------------------------")
    driver.find_element_by_id("feedTable_next").click()
    x = x + num
    y = y + num2
print("总共编辑了%d条" % y)
print("剩余%d条未编辑" % x)
end = datetime.datetime.now()
print("Running time:%s Second" % (end - start))
driver.close()
'''
# 键词的数组
yinsi = ["隐私", "私隐", "不想别人看", "隱私", "稳私", "让别人知道我在", "把自己看过的东西公布", "不想看",
         "我不想让朋友", "让朋友看不到", "泄露", "瘾私", ]
turnOff = ["关闭", "关掉", "不想要这个功能"]
sex = ["色情", "低俗"]
title = ["标题党", "文不对题", "张冠李戴", "标题与内容不符", "雷人标题","广告"]
chuanxiao = ["传销", "古币", "钱币"]
zongjiao = ["穆斯林", "基督"]
gupiao = ["推荐股票"]
vedio = ["视频打不开", "不能播放", "视频异常", "无法播放"]
kadun = ["视频无响应","视频卡"]
entry = ["找不到入口", "没有看一看", "看一看找不到", "没有入口", "找不到看一看", "没有找到入口", "看一看没有", "没有“看一看”", "没有‘看一看’", "没有\"看一看\""
    , "没有\'看一看\'"]
faxianye = ["发现页管理", "发现管理页"]
baiping = ["看一看白屏", "白屏", "什么都不显示", "刷新后无内容", "不显示内容"]
dabukai = ["看一看打不开"]
addNewFunction = ["红点", "全选", "浏览历史", "瀏覽歷史", "一键屏蔽"]
crash = ["闪退", "重启"]
heiping = ["黑屏"]
picture = ["图片打不开", "图片加载不了"]
neirong = ["质量", "垃圾", "文理不通", "乱七八糟"]
newPoint = ["红点消不了"]
word = ["文字", "字体"]
memory = ["占内存", "占空间"]
doc = ["文章打不开"]
false = ["虚假", "骗人"]
swindle = ["诈骗"]

for j in range(int(a)):
    num = 0
    num2 = 0

    for i in range(100):
        try:
            bianji = driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[" + str(i + 1) + "]/following::button[1]")
        except NoSuchElementException:
            # print("这页分完")
            break
        con = driver.find_element_by_xpath('// *[ @ id = "feedTable"] / tbody / tr[' + str(i + 1) + '] / td[6]')
        osCon = driver.find_element_by_xpath("//*[ @ id = 'feedTable']/tbody/tr[" + str(i + 1) + "]/td[3]")

        try:
            for a in yinsi:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("担心泄露隐私")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in neirong:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("内容质量差")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in swindle:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("传销诈骗")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in false:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("虚假信息")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in turnOff:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("想关闭看一看")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in heiping:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("看一看黑屏")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in crash:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("看一看闪退")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in sex:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("色情低俗")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in picture:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("图片加载不出")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in title:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("标题党")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in chuanxiao:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("传销诈骗")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in zongjiao:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("宗教反馈")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in gupiao:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("推股荐股")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in vedio:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("视频无法播放")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in kadun:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("视频卡顿")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in newPoint:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("红点消不了")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in word:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("字体反馈")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in doc:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("文章打不开")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in entry:
                if a in con.text:
                    if osCon.text[0] == "a":
                        os = osCon.text.split("-")
                        # logging.info("android os: " + str(os))
                        if int(os[1]) >= 27:
                            bianji.click()
                            driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                            bianji.click()
                            num2 = num2 + 1
                        else:
                            bianji.click()
                            driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                            bianji.click()
                            num2 = num2 + 1
                    elif osCon.text[0] == "i":
                        if osCon.text[1] == "O":
                            os = osCon.text.split(" ")
                            try:
                                osVersion = os[1].split(".")[0]
                                # logging.info("ios os: " + str(os) + ", isVersion: " + str(osVersion))
                            except IndexError:
                                continue
                            if int(osVersion) >= 12:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                bianji.click()
                                num2 = num2 + 1
                            else:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                bianji.click()
                                num2 = num2 + 1
                        elif osCon.text[1] == "P":
                            os = osCon.text.split(" ")

                            try:
                                osVersion = os[2].split(".")[0]
                            except IndexError:
                                raise KeyError
                            # logging.info("ios os: " + str(os) + ", isVersion: " + str(osVersion))
                            if int(osVersion) >= 12:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                bianji.click()
                                num2 = num2 + 1
                            else:
                                bianji.click()
                                driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                bianji.click()
                                num2 = num2 + 1
                    raise KeyError

            for a in dabukai:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("看一看打不开")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in baiping:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("看一看白屏")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in faxianye:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError

            for a in addNewFunction:
                if a in con.text:
                    bianji.click()
                    driver.find_element_by_id("mySelect").send_keys("新增功能反馈")
                    bianji.click()
                    num2 = num2 + 1
                    raise KeyError
        except KeyError:
            continue

        num = num + 1
    print("---------------------------------------")
    print("第%d页" % (j + 1))
    print("编辑%d条" % num2)
    print("未编辑%d条" % num)
    print("---------------------------------------")
    driver.find_element_by_id("feedTable_next").click()
    x = x + num
    y = y + num2
print("总共编辑了%d条" % y)
print("剩余%d条未编辑" % x)
end = datetime.datetime.now()
print("Running time:%s Second" % (end - start))
driver.close()