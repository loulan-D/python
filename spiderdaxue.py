"""
中国大学排名定向爬虫，对特定网页爬取目标内容。
技术路线---requests-bs4 "这一点非常好：首先分析要解决的问题，然后想出自己的技术路线，条理化"
‘程序的结构设计：1，获取网页内容getHtmlText()2,对网页内容进行解析，提取信息到合适的数据结构fillUnivList().3.输出结果printUnivList()’
首先写出一个mian函数，搭一个框架，然后再对框架进行填充；分别写getHtmlText(),fillUnivList(),printUnivlist().
优化代码，“输出结果的中文对齐问题”
"""
#spiderdaxue.py
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
#输出的结果不整齐！当中文字符宽度不够时，采用西文字符填充；中西文字符占用宽度不同，采用中文字符的空格填充c h r ( 1 2 2 8 8 )
#还不会用！   
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs
main()
