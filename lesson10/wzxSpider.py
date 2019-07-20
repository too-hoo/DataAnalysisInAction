# coding:utf-8
# 下载王祖贤的豆瓣图片
import requests
import json
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
for i in range(0, 24908, 20):
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+ str(i)
    html = requests.get(url).text       # 得到返回的结果
    response = json.loads(html,encoding='utf-8')  # 将json格式转换成为Python的对象
    for image in response['images']:  # 遍历得到的列表
        print(image['src']) # 查看当前下载的图片的地址
        download(image['src'],image['id'])  # 下载一张图片