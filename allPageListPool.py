#coding=utf-8
#url 地址缓存池
class AllPageListPool():
	"""docstring for UrlPool"""
	__urlPool = [] #url 内存池
	__instance = None
	def getInstance(cls):
		if cls.__instance:
			return cls.__instance
		else:
			cls.__instance = AllPageListPool()
			return cls.__instance

	def __init__(self):
		pass
		
	def appendUrlVo(self, vo):
		self.__urlPool.append(vo)
		pass

	def getUrlVo(self):
		return self.__urlPool.pop(0)

	def getLen(self):
		return len(self.__urlPool)
		