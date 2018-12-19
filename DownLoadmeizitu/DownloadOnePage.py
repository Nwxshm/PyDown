#coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.mzitu.com/26685'
header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
        'Referer':'http://www.mzitu.com'
        }
header2 = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
        'Referer':'http://i.meizitu.net'
        }
html = requests.get(url,headers = header)
soup = BeautifulSoup(html.text,'html.parser')

#最大页数在span标签中的第10个
pic_max = soup.find_all('span')[10].text
title = soup.find('h2',class_='main-title').text
for i in range(1,int(pic_max) + 1):
    href = url+'/'+str(i)
    html = requests.get(href,headers = header)
    mess = BeautifulSoup(html.text,"html.parser")


    #图片地址在img标签alt属性和标题一样的地方
    pic_url = mess.find('img',alt = title)
    pic_url['src'] = 'http://i.meizitu.net/2018/10/16c02.jpg'
    html = requests.get(pic_url['src'],headers = header2)

    #获取图片的名字方便命名
    file_name = pic_url['src'].split(r'/')[-1]
    Sava_path = "F:\\妹子图\\";
    if not (os.path.exists(Sava_path)):
        os.makedirs(Sava_path)
    fileName = Sava_path + file_name;
    #图片不是文本文件，以二进制格式写入，所以是html.content

    f = open(fileName, 'wb')
    f.write(html.content)
    f.close()