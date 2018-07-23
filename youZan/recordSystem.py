#coding=utf-8
def function(self, sourceVo):
	isEnd = False
	pageIndex = 1
	while isEnd==False:
	      isEnd = True
	      url = sourceVo.getUrlByPage(pageIndex)
	      aliasIds = goodListController.openGoodsUrl(url) #拿到当前页所有的商品信息列表
	      if len(aliasIds)>0:
	        #保存商品销售数据
	        # onePageData = sellInfoController.getOnePageAliasPrice(aliasIds, sourceVo)
	        onePageData = sellInfoController.getOnePageAliasInfo(aliasIds, sourceVo)
	        allPageList.append(onePageData)
	        pageIndex = pageIndex + 1
	      else:
	        isEnd = True
	pass