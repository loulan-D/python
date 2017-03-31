"""
爬取淘宝商品页面
技术路线  ---requests-re
理解淘宝爬虫的接口和翻页的处理
步骤：“提交请求循环获取每个网页的内容---对网页内容进行解析，获取目标信息---打印”
先写一个主函数搭一个框架.

"""
import requests
import re            # 正则表达式还不太会用

#获取一个网页内容，用try--except--框架
def getHtmlText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding= r.apparent_encoding
		return r.text
	except:
		return '' 
#
def parsePage(ilt,html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print("")
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count = 0
	for g in ilt:
		count = count +1
		print(tplt.format(count, g[0],g[1]))


def main():
	goods = "书包"
	depth = 3
	start_url = 'https://s.taobao.com/search?q='+goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHtmlText(url)
			parsePage(infoList,html)
		except:
			continue
	printGoodsList(infoList)
main()