# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: QQRobot
File Name: shuoshuo.py
Author: hhx
Contact: houhaixu_email@163.com
Create Date: 2021/3/1
-------------------------------------------------
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

##因为用到模拟浏览器，需要调用浏览程序
chromedriver = r"C:\Users\10219\Desktop\chromedriver.exe"
# option = webdriver.ChromeOptions()
# option.add_argument(r'user-data-dir=C:\Users\10219\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(10)
driver.get("https://qzone.qq.com/")
# 等待5秒后，判断页面是否需要登录，通过查找页面是否有相应的DIV的id来判断
try:
    driver.find_element_by_id('login_div')
    a = True
except:
    a = False
if a == True:
    # 如果页面存在登录的DIV，则模拟登录（遇到滑动的时候需要手动滑动，所以我在下面设置10秒）
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()  # 选择用户名框
    driver.find_element_by_id('u').send_keys('1021969591')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('hhx15966884268')
    driver.find_element_by_id('login_button').click()
    time.sleep(10)

    ##找到发说说按钮，进行点击
    driver.find_element_by_id("$1_substitutor_content").click()
    driver.find_element_by_id("$1_content_content").send_keys("表白条")
    driver.find_element_by_xpath(
        "/html[@class='skin-light']/body[@class='os-winxp bg-body date-20210301']/div[@id='layBackground']/div[@class='layout-background']/div[@class='layout-body']/div[@id='pageContent']/div[@id='main_feed_container']/div[@class='col-main-feed']/div[@id='QM_Mood_Poster_Container']/div[@id='QM_Mood_Poster_Inner']/div[@class='qz-poster-inner qz-poster-2021-03-01']/div[@class='qz-poster-ft']/div[@class='op']/a[@class='btn-post gb_bt  evt_click']").click()
    time.sleep(2)
try:
    driver.switch_to.frame('app_canvas_frame')  # 进入iFrame
    time.sleep(3)
    try:
        # 因为第一个找到的class无法点击，所以我们找到可以点击然后光标进入编辑框的，然后模拟点击
        driver.find_element_by_xpath('//*[@id="$1_substitutor_content"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="$1_content_content"]').send_keys("自动发说说功能")
        print('文字输入成功')
        time.sleep(0.5)
        ##点击发送按钮
        driver.find_element_by_xpath('//*[@id="QM_Mood_Poster_Container"]/div/div[4]/div[4]/a[2]').click()
        print('发送成功！')
    finally:
        print('OK！')

finally:
    print('End')
