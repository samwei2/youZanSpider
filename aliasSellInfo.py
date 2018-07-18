#coding=utf-8
import requests
import re
import json

class SellInfoController():
	"""docstring for SellInfoController"""
	__urlPath = "https://h5.youzan.com/v2/trade/order/orderitemlist.json?perpage=10&alias="
	__goodsId = "2ou1uu4wfyybx"
	__pageTab = "&page="
	__page = 1
	__pageArr = [] #当前商品订单数据总和
	__total = 0
	__has_next = True

	def __init__(self, headers, cookies):
		# print(" hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		# print(headers)
		# print(cookies)

		self.__headers = headers
		self.__cookies = cookies
		self.initData()
		return
		
	def initData(self):

		return

	def checkAliasInfo(self, aliasId, aliasTitle, allOrOne=1):
		self.__goodsId = aliasId
		# __page = page
		# if page==null:
		self.__page = 1 #从第一页开始抓数据
		self.__pageArr = []
		self.__total = 0
		self.__has_next = True
		# 	pass
		# print(self.__urlPath + self.__goodsId + self.__pageTab + str(self.__page))

		url = ""
		while self.__has_next==True:
			url = self.__urlPath + self.__goodsId + self.__pageTab + str(self.__page)
			print("url ready...", url)
			resp = requests.get(url, headers=self.__headers, cookies=self.__cookies)
			res = resp.content.decode('utf-8')

			print("html ..decodeing")
			s = json.loads(res)
			print("html ..decode end")

			dataList = s['data']['list'] 
			self.__has_next = s['data']['has_next']
			print("hes_next..", self.__has_next)

			if self.__total==0:
				self.__total = int(s['data']['total'])
				pass

			# print(s)
			# 
			index = 0
			for line in dataList:
				lineData = {}
				# print line
				index = index + 1
				lineData['uid'] = aliasId + "&p"+ str(self.__page) +"&i"+ str(index)
				lineData['data'] = line
				lineData['title'] = aliasTitle #传一个商品名称进来
				self.__pageArr.append(lineData)	
				# print(lineData['uid'])
			pass

			self.__page = self.__page + 1
			if self.__page>100:
				break
		pass

		print(url + "..all data is completed..")
		

		return self.__pageArr, self.__total


