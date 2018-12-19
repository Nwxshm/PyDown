#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
    'Referer':'http://www.mmjpg.com/'
}
header2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
    'Referer':'http://www.mmjpg.com'
}
# all_url = 'http://www.mmjpg.com/more/'
all_url = 'http://www.mmjpg.com/top/'
# all_url = 'http://www.mmjpg.com/hot/'
# all_url = 'http://www.mmjpg.com/'
start_html = requests.get(all_url, headers = header)
soup = BeautifulSoup(start_html.text, "lxml")
list_page = soup.find_all('li')
n = 1
for page in list_page:
    list_url = page.find('a')['href']
    print(list_url)
    list_html = requests.get(list_url, headers=header)
    list_html.encoding = 'utf-8'
    soup = BeautifulSoup(list_html.text, "lxml")
    title = soup.find('h2').get_text()
    print(title)
    a = soup.find('div',class_='page').find_all('a')
    max_page_a = a[-2].get_text()
    print(max_page_a)
    path = 'f:/MMjpg/{0}/'.format(title)
    if not (os.path.exists(path)):
         os.makedirs(path)
    for i in range(1,int(max_page_a)+1):
         url = list_url + '/{0}'.format(str(i))
         html = requests.get(url, headers=header)
         html.encoding = 'utf-8'
         soup = BeautifulSoup(html.text, "lxml")
         img = soup.find('div', class_='content').find('a').find('img')
         downUrl = img['src']
         print(downUrl)
         pic_html = requests.get(downUrl, headers=header2)
         filename = downUrl.split(r'/')[-1]
         f = open(path+filename, 'wb')
         f.write(pic_html.content)
         f.close()
         print("第"+str(n)+"个----第"+str(i)+"页下载完毕")
    n = n + 1