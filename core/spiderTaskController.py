#coding=utf-8
# 定期处理任务的控制器
class SpiderTaskController():
	"""docstring for spiderTaskController"""
	__loopTime = 500
	__lastTime = 0
	__addTime = 0
	__taskList = []
	def __init__(self):
		for x in xrange(1,10):
			self.addTask(())
			pass
		pass
		
	def updateTask(self, lastTime, addTime):
		if len(self.__taskList)>1:
			if self.__addTime<self.__loopTime:
				self.__addTime = self.__addTime + addTime
			else:
				self.toTask()
				self.__addTime = 0


	# 执行一个任务
	def toTask(self):
		taskVo = self.__taskList.pop(0)
		print("decode task")
		pass

	# 添加一个任务
	def addTask(self, taskVo):
		self.__taskList.append(taskVo)
		pass
		