# -*- coding:utf-8 -*-
import time
from selenium import webdriver
browser = webdriver.Chrome("/home/toohoo/Desktop/chromedriver_linux64/chromedriver")
# 登录微博
def weibo_login(username, password):
     # 打开微博登录页
     browser.get('https://passport.weibo.cn/signin/login')
     browser.implicitly_wait(5)
     time.sleep(1)
     # 填写登录信息：用户名、密码
     browser.find_element_by_id("loginName").send_keys(username)
     browser.find_element_by_id("loginPassword").send_keys(password)
     time.sleep(1)
     # 点击登录
     browser.find_element_by_id("loginAction").click()
     time.sleep(1)
# 设置用户名、密码
username = 'username'
password = "********"
weibo_login(username, password)


