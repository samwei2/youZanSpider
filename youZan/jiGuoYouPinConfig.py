#coding=utf-8
# kdt_id = 16975645

from youZanWebBaseConfig import YouZanWebBaseConfig
class JiGuoYouPinConfig(YouZanWebBaseConfig):
	"""docstring for AA"""
	def __init__(self):
		self.kdt_id = "19260293"
		self.dataBaseTable = "alias_jiguoyoupin"
		print("现在开始装配  极果优品数据。。。。。。。。")
		print("首页地址："+self.getUrlByPage(1))
		pass