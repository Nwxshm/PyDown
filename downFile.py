#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
def Download(href,header,title,path):
    os.makedirs(path)
    os.chdir(path)
    html = requests.get(href, headers=header)
    print(html)
    file_name = 'test1.mp4'
    f = open(file_name,'wb')
    f.write(html.content)
    f.close()
    print('完成'+title)
if __name__=='__main__':
    if (os.name == 'nt'):
        print(u'你正在使用win平台')
    else:
        print(u'你正在使用linux平台')

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
        'Referer': 'http://v.baidu.com'
    }
    header2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36',
        'Referer': 'http://v.baidu.com'
    }
    # http请求头
    path = 'F:/DownFile/'
    href = 'http://v.baidu.com/watch/7982758475243349681.html?fr=v.baidu.com/channel/amuse';
    title = '搞笑';
    #线程池中线程数
    pool = Pool(10)
    pool.apply_async(Download,args=(href,header2,title,path))
    pool.close()
    pool.join()
    print('已下完')
