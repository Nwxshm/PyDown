from bs4 import BeautifulSoup as bs
import urllib.request as ur

baseUrl = "https://fanyi.baidu.com"
Form_Data = {}
Form_Data = {
    'from': 'en',
    'to': 'zh',
    'query': 'jack',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '143778.447123',
    'token': 'c39af1d0743fc4d6184a960719419f52'
}
url = baseUrl+'/#{0}/{1}/{2}'.format(Form_Data['from'], Form_Data['to'], Form_Data['query'])
print(url)
res = ur.urlopen(url)
html = res.read().decode('utf-8')
print(html)