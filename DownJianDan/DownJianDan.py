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
dir = 'F:/jiandan-girls/'
if not (os.path.exists(dir)):
    os.makedirs(dir)
img_urls = []
page_urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(1, 40)]
header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
        }
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

def DownloadImg():
    n = 1
    for i in img_urls:
        print('第 ' + str(n) + ' 张 ... ', end='')
        with open(dir + i[-20:], 'wb') as f:
            f.write(requests.get(i).content)
        print('OK!')
        n = n + 1

for u in page_urls:
    GetImgUrl(u)
print('*** 开始下载 ***')
DownloadImg()
print('*** 下载完成 ***')