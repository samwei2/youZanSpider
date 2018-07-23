# 存储商家池
class ShangJiaPool():
	"""docstring for ShangJiaPool"""
	__shangjiaList = ()
	def __init__(self):
		super(ShangJiaPool, self).__init__()
	
	# 添加一个新的商铺	
	def addShangJia(self, vo):
		self.__shangjiaList.append(vo) 
	
	# 获取第一家商铺
	def getShangjia(self):
		return self.__shangjiaList.pop(0)

	# 等待抓取的商铺数目
	def getLen(self):
		return len(self.__shangjiaList)