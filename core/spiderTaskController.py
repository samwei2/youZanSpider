#coding=utf-8
# 定期处理任务的控制器
class SpiderTaskController():
	"""docstring for spiderTaskController"""
	__tasksDic = {} 
	__loopTimeMapping = {} #时间间隔映射
	ADD_TASK = 500
	RECORD_PAGE = 100
	def __init__(self):
		# for x in xrange(1,10):
		# 	self.addTask(())
		# 	pass
		self.initLoopMapping("ADD_TASK", self.ADD_TASK)
		self.initLoopMapping("ARECORD_PAGE", self.RECORD_PAGE)
		self.initLoopMapping("RECORD_DATABASE", self.RECORD_PAGE)
		pass
		
	def updateTask(self, lastTime, addTime):
		tmpAddTime = 0
		tmpLoopTime = 0
		# try:
		for sTaskType in self.__tasksDic:
			taskList = self.__tasksDic[sTaskType]
			if len(taskList)>0:
				tmpAddTime = self.getLoopTimeBysTask(sTaskType)[0]
				tmpLoopTime = self.getLoopTimeBysTask(sTaskType)[1]
				# print(tmpAddTime, tmpLoopTime)
				if tmpAddTime<tmpLoopTime:
					tmpAddTime += addTime
					# print(tmpAddTime)
					self.setLoopMapping(sTaskType, tmpAddTime)
				else:
					self.toTaskByType(sTaskType)
					self.setLoopMapping(sTaskType,0)
		# except Exception as e:
		# 	print("updateTask error", e.message)
		# 	pass

		

	def addTaskByType(self, sTaskType, taskVo):
		self.__tasksDic[sTaskType].append(taskVo)
		# print("addTasklT", self.__tasksDic[sTaskType])
		pass
		
	def toTaskByType(self, sTaskType):
		# print("do sTaskType", sTaskType , self.__tasksDic[sTaskType])
		if len(self.__tasksDic[sTaskType])<1:
			print("chang du buzu")
			return
		taskVo = self.__tasksDic[sTaskType].pop(0)
		func = taskVo['func']
		func(taskVo['param'][0],taskVo['param'][1])
		print("decode task")

	def initLoopMapping(self, sTaskType, loopTime=1000):
		self.__loopTimeMapping[sTaskType] = [0, loopTime]
		self.__tasksDic[sTaskType] = []
	
	def setLoopMapping(self, sTaskType, addTime):
		if self.__loopTimeMapping[sTaskType] is None:
			self.initLoopMapping(sTaskType)
		self.__loopTimeMapping[sTaskType][0] = addTime

	def getLoopTimeBysTask(self, sTaskType):
		if self.__loopTimeMapping[sTaskType] is None: return 0
		return self.__loopTimeMapping[sTaskType]



