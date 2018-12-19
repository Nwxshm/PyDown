import os
import time
from urllib import request
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup as bs

class BaiduSearch():
    def __init__(self,searchText=''):
        self.driver = webdriver.PhantomJS()
        self.searchText = searchText
        print("init success")
    def __del__(self):
        try:
            self.driver.close()
            self.driver.quit()
            print('webdriver close and quit success!')
        except:
            pass
    def _auto_scroll_to_bottom(self):
        '''
        将当前页面滑动到最底端
        '''
        js = "var q=document.body.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(6)

    def _search(self):
        self.driver.get("http:www.baidu.com")
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys(self.searchText)
        self.driver.find_element_by_id('su').click()
        try:
            if not(self.driver.find_element_by_id('kw')==None):
                return True
            else:
                return False
        except:
            return False

    def _getList(self):
        hrefs = []
        if(self._search()):
            self.driver.get("http:www.baidu.com?wd={0}".format(self.searchText))
            self._auto_scroll_to_bottom()
            html = self.driver.page_source
            #soup = bs(html, 'hxml.parser')
            #result = soup.find_all('a')
            print(html)
            # for content in result:
            #     href = content.get('href')
            #     hrefs.append(href)
        print(hrefs)

if __name__ == '__main__':
    BaiduSearch('头像')._getList()