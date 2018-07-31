#coding=utf-8
import time
# import sleep
from spiderTaskController import SpiderTaskController

# 蜘蛛程序主循环
class SpiderCore():
	"""docstring for SpiderCore"""
	__lastTime = 0
	__overflow = 0
	__frameTime = 16
	__isRunning = True #心跳执行状态

	def init(self):
		self.__lastTime = self.getCurTime()
		self.spiderTaskController = SpiderTaskController()
		pass
	
	# 爬虫主循环
	def start(self):
		import threadTimer
		def toRound(curTime, lastTime):
			self.__lastTime = curTime
			_addTime = curTime - lastTime + self.__overflow
			if _addTime>=self.__frameTime:
				overflow = _addTime - self.__frameTime
				# print(self.__lastTime, _addTime)
				self.spiderTaskController.updateTask(self.__lastTime, _addTime)
			pass
		self.__lastTime = int(round(time.time() * 1000))
		if self.getRunningState() == False:
			threadTimer.heart_beat(None, 0, False)
		else:
			threadTimer.heart_beat(toRound,self.__lastTime)

	def getRunningState(self):
		return self.__isRunning

	def stop(self):
		self.__isRunning = False

	def getSpiderTaskController(self):
		return self.spiderTaskController


	def getCurTime(self):
		return int(round(time.time() * 1000))

# def printd(param1, param2):
# 	print(param1, param2)
# 	pass
# dd = SpiderCore()
# dd.init()
# dd.start()
# aa = SpiderTaskController()
# aa.addTaskByType("ADD_TASK",{'func':printd, "param":(1,2)})
# print("IIIIIIIIIi")
# aa.addTaskByType("ARECORD_PAGE",{'func':printd, "param":(22222,000000)})
