import urllib.request as ur
from bs4 import BeautifulSoup
import os
def get_content(url):
    html = ur.urlopen(url)
    content = html.read().decode('utf-8')#转码
    html.close()#记得要将打开的网页关闭，否则会出现意想不到的问题
#    print (type(content))
    return content
def get_image(info):
    '''
    利用Soup第三方库实现抓取
    '''
    soup = BeautifulSoup(info,"lxml")#设置解析器为“lxml”
    all_image = soup.find_all('img')
    x=1
    for image in all_image:
        print(all_image)
        save_path = "f:\\photo\\"
        if not(os.path.exists(save_path)):
            os.makedirs(save_path)
        ur.urlretrieve(image['src'], save_path+"%s.jpg"%(x))
        x+=1
url = "http://jiandan.net/ooxx"
info = get_content(url)
print (info)
get_image(info)
