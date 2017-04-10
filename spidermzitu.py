# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:38:25 2017

@author: loulan
"""
"""
#完整代码  学习源于http://cuiqingcai.com
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
start_url = "http://www.mzitu.com/all"
r = requests.get(start_url, headers = headers)
#print (r.text)
Soup = BeautifulSoup(r.text,'lxml')
#li_list = Soup.find_all('li')
#for li in li_list:
  #  print (li)
all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
    path = str(title).strip()
    href = a['href']
    os.makedirs(os.path.join("D:\mzitu", path)) ##创建一个存放套图的文件夹
    os.chdir("D:\mzitu\\"+path) 
    now_html =requests.get(href,headers = headers)
    now_soup =BeautifulSoup(now_html.text,'lxml')
    now_span =now_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    for page in range(1, int(now_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
        page_url = href + '/' + str(page) ##同上
        img_html =requests.get(page_url,headers=headers)
        img_soup =BeautifulSoup(img_html.text,'lxml')
        img_url = img_soup.find('div',class_='main-image').find('img')['src']
        name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content) ##多媒体文件要是用conctent哦！
        f.close()
        print (name)
"""
"""
#写几个函数，现在还不太会用
import requests
from bs4 import BeautifulSoup
import os

class mzitu():
    def all_url(self,url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title=a.get_text()
            print(u'start save:',title)
            path = str(title).replace("?","_")
            self.mkdir(path)
            href = a['href']
            self.html(href)
    def html(self,href):
        html = self.request(href)
        max_span = BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):
            page_url = href + '/' + str(page)
            self.img(page_url)
    def img(self,page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)
    def save(self,img_url):
        name = img_url[-9:-4]
        img= self.request(img_url)
        f = open(name + '.jpg','ab')
        f.write(img.content)
        f.close()
    
    def mkdir(self, path): ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            os.chdir(os.path.join("D:\mzitu", path)) ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False
    def request(self, url): ##这个函数获取网页的response 然后返回
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content

Mzitu = mzitu() ##实例化
Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数 

"""
"""
#用functions进行封装

"""
#用requests库获取网页源码，用bs4对网页进行解析
#1用requests库获取网页源码；2，利用开发者调试工具在html文件中查看目标内容；3，用beautifulsoup方法获取目标内容
#一个过程，一步步调试
import requests  #导入requests
from bs4 import BeautifulSoup   #导入beautiful
import os

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}  #浏览器请求头
start_url = "http://www.mzitu.com/all"
r = requests.get(start_url,headers=headers)
r.encoding=r.apparent_encoding
#print(r.text)#(请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
'''
#也可以用一个requests.get()框架，中国mooc上学的
#做异常处理，但是出错了
try:
    r=requests.get(start_url,headers=headers)
    r.raise_for_status()
    t.encoding=r.apparent_encoding
    print(r.text)
except:
    print("error")
'''
"""
soup = BeautifulSoup(r.text,'lxml')  #创建一个bs4对象soup，利用beautifulsoup方法对获取的网页源码进行解析
li_list= soup.find_all('li')      #用find_all方法查找html文件中所有的li标签，返回的是一个列表，
for li in li_list:
    print(li)
"""
all_a = soup.find('div',class_='all').find_all('a')   #直接查找所有的目标a标签
for a in all_a:
    title = a.get_text()#获取目标地址的标题
    path = str(title).strip() ##去掉空格
    os.makedirs(os.path.join("D:\mzitu", path)) ##创建一个存放套图的文件夹
    os.chdir("D:\mzitu\\"+path) ##切换到上面创建的文件夹
    href=a['href']#获取目标连接
    html = requests.get(href,headers=headers)
    html_soup=BeautifulSoup(html.text,'lxml')
    max_span=html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        img_html = requests.get(page_url,headers=headers)
        img_soup = BeautifulSoup(img_html.text,'lxml')
        img_url = img_soup.find('div',class_='main-image').find('img')['src']
        #print(img_url)到这里就已经获得了目标图标，接下来就是保存图片
        name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！
        f.write(img.content) ##多媒体文件用conctent
        print(name)
        f.close()
  
    






