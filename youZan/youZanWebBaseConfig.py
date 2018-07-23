#coding=utf-8
#有赞网站的基础设定
class YouZanWebBaseConfig():
	"""docstring for YouZanWebBaseConfig"""

	urlHead = "https://h5.youzan.com/v2/showcase/goods/allgoods?"
	aliasUrlHead = "https://detail.youzan.com/show/goods?alias="
	kdt_id = ""
	dataBaseTable = ""

	def __init__(self):
		pass

	def getUrlByPage(self, page):
		tmpUrl = self.urlHead + "kdt_id="+self.getKdtId() + "&p=" + str(page)
		return tmpUrl
	
	# 获取商品地址
	def getAliasLink(self, aliasId):
		return self.aliasUrlHead + aliasId

	# 获取店铺 kdt_id(不同商家，都由kdt_id区分)
	def getKdtId(self):
		return self.kdt_id

    # 获取数据库表名
	def getTableName(self):
		return self.dataBaseTable