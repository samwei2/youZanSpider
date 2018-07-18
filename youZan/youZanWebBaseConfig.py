#coding=utf-8
#有赞网站的基础设定
class YouZanWebBaseConfig():
	"""docstring for YouZanWebBaseConfig"""

	urlHead = "https://h5.youzan.com/v2/showcase/goods/allgoods?"
	kdt_id = ""

	def __init__(self):
		pass

	def getUrlByPage(self, page):
		tmpUrl = self.urlHead + "kdt_id="+self.getKdtId() + "&p=" + str(page)
		return tmpUrl
	
	#获取店铺 kdt_id(不同商家，都由kdt_id区分)
	def getKdtId(self):
		return self.kdt_id