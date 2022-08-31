#pip install beautifulsoup4
import requests
import re
import os
import time
from bs4 import BeautifulSoup

'''
				NOTE

#		print(soup.prettify())	#格式化输出
#		one_info.h2.get_text()	#唯一项时可以精确获取字符
#		one_info.a['href'])	#获取标签内的属性值
#	<a class="" data-v-7f856186="" href="/detail/1">
#	<img class="cover" data-v-7f856186="" src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c"/>
#	</a>
#		soup.find_all('div','el-card item m-t is-hover-shadow')	llist format
		sout.find('div','test') 	
'''

class spider_web:
	def __init__(self,url,User_Agent,content_type,username,password):
		self.url = url
		self.User_Agent = User_Agent
		self.content_type = content_type
		self.header = {'User-Agent':self.User_Agent,
						'content_type':self.content_type}
		self.username = username
		self.password = password
		self.basic_auth = requests.auth.HTTPBasicAuth(self.username,self.password)

	def get_one_page(self):
#		抓取页面

		page = requests.get(self.url,auth=self.basic_auth,headers=self.header)

#		将TXT格式的文件进行 LXML 格式转换， soup.prettfy()按照标准XML格式输出

		soup = BeautifulSoup(page.text,'lxml')


#		print (soup.div['id'])
		all_info = soup.find_all('div','el-card item m-t is-hover-shadow')
		one_info = soup.find('div','el-card item m-t is-hover-shadow')

		def has_span_not_class(self):
			return  not one_info.has_attr('class')

		print(one_info)
		print(one_info.h2.get_text())
		print(one_info.span.get_text())
		print(str(one_info.img['src']))
		print('*'*100)
		print(one_info.find('div','categories').find_all('span'))
		print(one_info.find('div','m-v-sm info').find_all('span'))
		for i in all_info:
#			print(i.find('class'.''))
#			video_name = i.h2.get_texxt()
#			video_link = i.a.get_text()
#			pic_link = i.img['src']
			print('*'*100)
#		print(soup.find('div','el-card item m-t is-hover-shadow'))



	def url_manager():
		print("url_manager")


	def storage(self):
		print("storage")


if __name__ =='__main__':
	url = 'https://ssr3.scrape.center/'
	User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
#	content_type = 'application/json; charset=utf8'
	content_type = 'text/html;charset=utf-8'
	username = 'admin'
	password = 'admin'

	spider = spider_web(url,User_Agent,content_type,username,password)
	spider.get_one_page()
