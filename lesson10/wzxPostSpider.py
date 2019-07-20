# coding:utf-8
# 下载王祖贤的电影封面海报
import requests
import json
from lxml import etree

# 配置selenium
from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")  # 隐身模式打开
# driver_path = "/home/toohoo/Desktop/chromedriver_linux64/chromedriver"  # chromedriver的路径
driver = webdriver.Chrome("/home/toohoo/Desktop/chromedriver_linux64/chromedriver")

query = "王祖贤"
'''下载图片'''
def download(src,id):
    # 将图片写到当前目录，原来的图片的格式是webp的，需要转换一下格式
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir,'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载！')

'''for 循环 请求全部的url'''
request_url = 'https://www.douban.com/search?cat=1002&q=' + query
driver.get(request_url)

# 注意是这样写的！
html = etree.HTML(driver.page_source)

srcs = html.xpath("//div/a[@class='nbg']/img/@src ")
titles = html.xpath("//div[@class='title']/h3/a/text()")

for src,title in zip(srcs, titles):
    # 调用的时候记得转换编码！！
    download(src, title.encode("utf-8"))