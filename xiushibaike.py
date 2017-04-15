# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:27:15 2017

@author: loulan
"""
"""
#version1


#输入要打印的页数，然后开始打印糗事百科的内容
import requests
from bs4 import BeautifulSoup
print("工作之余，来看几个笑话吧！\n")
i = int(input("请输入你要打印的页数\n"))
for page in range(i):
    url = "http://www.qiushibaike.com/8hr/page/"+str(page)+"/?s=4973530"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    start_html = requests.get(url,headers = headers )
    soup = BeautifulSoup(start_html.text,'html.parser')
    content = soup.find_all('div',class_="content")
    for con in content:
        print(con.get_text())
"""
"""
#version2


import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    start_url = requests.get(url ,headers = headers)
    html = start_url.text
def get_content(html):
    soup = BeautifulSoup(start_html.text,'html.parser')
    soup = BeautifulSoup(start_html.text,'html.parser')
    content = soup.find_all('div',class_="content")
    for con in content:
        print(con.get_text())
print("工作之余，来看几个笑话吧！\n")
def main():
    page = int(input("请输入要打印的页数"))
    url = "http://www.qiushibaike.com/8hr/page/"+str(page)+"/?s=4973530"
    html=get_html(url)
    get_content(html)
main()
"""

#version3

"""
#实现目标eg：
1....（笑话）
    1.楼回复：...
2....（笑话）
"""
"""
import requests
from bs4 import BeautifulSoup
page = 1
while True:
    print("输入exit退出，输入enter进入下一页\n")
    raw = input("")
    if raw == "exit":
        break
    start_url = "http://www.qiushibaike.com/8hr/page/"+str(page)+"/?s=4974059"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    start_html = requests.get(start_url,headers = headers)
    soup = BeautifulSoup(start_html.text,'lxml')
    content = soup.find_all(attrs= "content")
    for content in content:
        print(content.get_text())
    page+=1

"""
"""
#version4
import requests
from bs4 import BeautifulSoup
page =1
while True:
    print("输入exit退出，输入enter观看下一页\n")#提示
    raw = input("")
    if raw == "exit":
        break
    url = "http://www.qiushibaike.com/8hr/page/{}/?s=4974059".format(page)
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    html = requests.get(url,headers = headers)
    soup = BeautifulSoup(html.text,'lxml')
    article_soup = soup.find_all(attrs = 'content')
    print("这是第%d页"%page)
    floor=1
    for article in article_soup:
        print(floor,".",article.get_text().strip())
        print("\n")
        floor+=1
    page+=1
"""
"""
#version5
"""
完善交互，增加类和方法，对代码进行优化和封装
"""
import requests
from bs4 import BeautifulSoup
import time   #防反爬处理
#糗事百科类
class QSBK(object):
    def get_article(self,url):
        try:#异常处理
            self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
            self.start_html = requests.get(url,headers = self.headers)
            self.start_html.raise_for_status()
            self.start_html.encoding = self.start_html.apparent_encoding
            self.start_text=self.start_html.text
        except:
            print("error")
        self.soup = BeautifulSoup(self.start_text,'lxml')
        all_url = self.soup.find_all(attrs = "content")
        for article in all_url:
            print("**"+article.get_text().strip())
            print("\n")
    def main(self):
        num = int(input("Do you want to how many pages?"))
        for page in range(num):
            self.start_url = "http://www.qiushibaike.com/8hr/page/{}/?s=4974160".format(page)
            self.get_article(self.start_url)
            raw=input("输入exit退出；输入enter显示下一页")
            if raw == "exit":
                break
            time.sleep(2)  #防反爬处理，爬取一个页面后等待2秒后再次爬取，不过前面进行了用户输入，应该好多了另外做练习使用，不必爬取大量页面，浪费流量
    
if __name__ == "__main__":
    qiushi = QSBK()
    qiushi.main()
"""





















