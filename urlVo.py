#coding=utf-8
class UrlVo():
	"""docstring for ClassName"""
	__url = ""
	__param = None
	def __init__(self, url, param):
		self.__url = url
		self.__param = param
		pass

	def getUrl(self):
		return self.__url

	def getParam(self):
		return self.__param