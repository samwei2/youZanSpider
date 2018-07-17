#coding=utf-8
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

from bs4 import BeautifulSoup
import js2xml

class GoodListController():
	
	__url = ""
	__headers = {}

	def __init__(self, headers):
		__headers = headers
		return

	def openGoodsUrl(self, url):
		__url = url
		driver = webdriver.Chrome() 


		driver.get(__url)

		htmlText = driver.page_source

		soup = BeautifulSoup(htmlText,"html.parser")

		script = soup.body.script

		sou = re.findall(r'\"alias\":\"(\w+)', script.string)
		title = re.findall(r'\"title":\"(.+?)\"', script.string)

		# for x in sou:
		# 	print x
		# pass

		# for x in title:
		# 	print x.decode('unicode_escape')
		# 	pass

		driver.quit()
		return sou, title



# url = "https://h5.youzan.com/v2/allgoods/16975645?reft=1531274513986&spm=f70430959"





