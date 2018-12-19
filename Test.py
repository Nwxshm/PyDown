import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.PhantomJS()
def GetImgUrl(u):
    driver.get(u)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('a.view_img_link')
    for i in images:
        t = i.get('href')
        if str('gif') in str(t):
            pass
        else:
            img_url = 'http:' + t
            img_urls.append(img_url)

for i in range(1,40):
    img_urls = []
    dir = 'F:/jiandan-girls/{}/'.format(str(i))
    if not (os.path.exists(dir)):
        os.makedirs(dir)
    url = "http://jandan.net/ooxx/page-{}#comments".format(str(i))
    GetImgUrl(url)
    print('*** 开始下载 ***')
    n = 1
    for j in img_urls:
        pic_name = "pic"+str(n)+".jpg"
        print('第 ' + str(i) + ' 页 ... '+'第 ' + str(n) + ' 张 ... ', end='')
        with open(dir+pic_name, 'wb') as f:
            f.write(requests.get(j).content)
        print('OK!')
        n = n + 1
    print('*** 下载完成 ***')