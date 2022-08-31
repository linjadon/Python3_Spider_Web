import requests
import re
import os
import time
from bs4 import BeautifulSoup



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
#		print(soup.prettify())

		print (soup.div['id'])
		print(soup.find_all(id='app'))


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