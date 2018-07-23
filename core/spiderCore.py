#coding=utf-8
import time
from spiderTaskController import SpiderTaskController
# 蜘蛛程序主循环
class SpiderCore():
	"""docstring for SpiderCore"""
	__lastTime = 0
	__overflow = 0
	__frameTime = 16  #1帧
	
	def init(self):
		self.__lastTime = self.getCurTime()
		self.spiderTaskController = SpiderTaskController()
		pass
	
	# 爬虫主循环
	def start(self):
		while 1:
			_addTime = self.getCurTime() - self.__lastTime + self.__overflow
			if _addTime>=self.__frameTime:
				self.__overflow = _addTime - self.__frameTime
				self.__lastTime = self.getCurTime()
				# print(self.__lastTime, _addTime)
				self.spiderTaskController.updateTask(self.__lastTime, _addTime) #
		
	
	def getCurTime(self):
		return int(round(time.time() * 1000))

dd = SpiderCore()
dd.init()
dd.start()