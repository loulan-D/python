# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:22:48 2017

@author: loulan
"""
#目标网站http://tieba.baidu.com/p/2166231880，在知乎上看到的例子，但是知乎的代码不全，决定自己练手自己敲
#目标依据spidermzitu的例子下载贴吧的图片，然后保存到本地
#实现思路：1用requests获取网站源码；2，用beautifulsoup对html文件进行解析获取目标图片；3，保存
#没有利用os模块，用os模块时总是出错，把os模块看看，然后对这个文件再进行优化
import requests
from bs4 import BeautifulSoup


start_url = "http://tieba.baidu.com/p/2166231880"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
html = requests.get(start_url,headers =headers)
html.encoding = html.apparent_encoding

soup = BeautifulSoup(html.text,'lxml')
all_img = soup.find('div',class_='left_section').find_all('img')
for img in all_img:
               
        src = img['src']
        name = src[-9:-4]
        img = requests.get(src,headers=headers)
        f = open(name +'.jpg','ab')
        f.write(img.content)
        print(name)
        f.close
