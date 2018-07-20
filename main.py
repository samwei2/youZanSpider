#coding=utf-8
from allGoodsList import GoodListController
from aliasSellInfo import SellInfoController
from mySqlController import SqlOperationController
import pymysql.cursors
import json

from youZan.zuiHeiKeJiConfig import ZuiHeiKeJiConfig
from youZan.chaPingConfig import ChaPingConfig

# 全局头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE"
}

#请求头
f = open('foo.txt')
cookies={}
for line in f.read().split(';'): 
    name,value=line.strip().split('=',1)
    cookies[name]=value

# print cookies

#商品控制
goodListController = GoodListController(headers)

sellInfoController = SellInfoController(headers, cookies)

sqlOperationController = SqlOperationController()

#商品道具列表
allPageList = []
#商品价格列表
allAliasPriceList = []

#取得最黑科技的数据
sourceVo = ZuiHeiKeJiConfig()
#差评的数据
# sourceVo = ChaPingConfig()

isEnd = False
pageIndex = 1
while isEnd==False:
      url = sourceVo.getUrlByPage(pageIndex)
      aliasIds = goodListController.openGoodsUrl(url) #拿到当前页所有的商品信息列表
      if len(aliasIds)>0:
        #保存商品销售数据
        onePageData = sellInfoController.getOnePageAliasPrice(aliasIds, sourceVo)
        allPageList.append(onePageData)
        pageIndex = pageIndex + 1
      else:
        isEnd = True


# # 没有数据库的话可以打开这条
# # sqlOperationController.createTable()

# for onePageData in allPageList:
#     aliasTitleDic = onePageData['aliasTitleDic']
#     sellInfoDic = onePageData['sellInfoDic']
#     sellTotalDic = onePageData['sellTotalDic'] 
#     sqlOperationController.saveAliasInfo(aliasTitleDic, sellInfoDic, sellTotalDic)
#     pass

if len(allPageList)>0:
    # 链接数据库
    sqlOperationController.connectSql()
    sqlOperationController.saveAllAliasPriceInfo(allPageList)
    sqlOperationController.closeLinkSql()
    pass

print("欢乐的时光总是过得特别快，Happy times always had a particularly fast")
