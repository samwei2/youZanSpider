#coding=utf-8
# kdt_id = 16975645

from youZanWebBaseConfig import YouZanWebBaseConfig
class ZuiHeiKeJiConfig(YouZanWebBaseConfig):
	"""docstring for AA"""
	def __init__(self):
		self.kdt_id = "16975645"
		self.dataBaseTable = "alias_zuiheikeji"
		print("现在开始装配  最黑科技数据。。。。。。。。")
		print("首页地址："+self.getUrlByPage(1))
		pass