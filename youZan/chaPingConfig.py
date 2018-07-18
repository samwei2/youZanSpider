#coding=utf-8
# kdt_id = 15311495

from youZanWebBaseConfig import YouZanWebBaseConfig
class ChaPingConfig(YouZanWebBaseConfig):
	"""docstring for AA"""
	def __init__(self):
		self.kdt_id = "15311495"
		print("现在开始装配  差评数据。。。。。。。。")
		print("首页地址："+self.getUrlByPage(1))
		pass