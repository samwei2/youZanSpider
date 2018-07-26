#coding=utf-8
from allGoodsList import GoodListController
from aliasSellInfo import SellInfoController
from mySqlController import SqlOperationController
# import c.cursors
import json

from youZan.zuiHeiKeJiConfig import ZuiHeiKeJiConfig
from youZan.chaPingConfig import ChaPingConfig

import urlPool
import core.spiderCore
import allPageListPool

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

spiderCore = core.spiderCore.SpiderCore()
spiderCore.init()
spiderCore.start()
print("coun+++++++++++====t")

sqlOperationController = SqlOperationController()

#商品道具列表
allPageList = []
#商品价格列表
allAliasPriceList = []

#取得最黑科技的数据
sourceVo = ZuiHeiKeJiConfig()
#差评的数据
# sourceVo = ChaPingConfig()


urlPool = urlPool.UrlPool()
isEnd = False
pageIndex = 1
while isEnd==False:
      # isEnd = True
      url = sourceVo.getUrlByPage(pageIndex)
      aliasIds = goodListController.openGoodsUrl(url) #拿到当前页所有的商品信息列表
      urlPool.appendUrlVo(url, aliasIds)
      if len(aliasIds)>0:
      #   #保存商品销售数据
          def decodeOnPageDataFunc(aliasIds, sourceVo):
              # onePageData = sellInfoController.getOnePageAliasPrice(aliasIds, sourceVo)
              onePageData = sellInfoController.getOnePageAliasInfo(aliasIds, sourceVo)
              # allPageList.append(onePageData)
              def recordDatabase(allPageList, sourceVo):
                  print("链接数据库--------------->")
                  # 链接数据库
                  sqlOperationController.connectSql()
                  # 判断数据库是否存在
                  sqlOperationController.checkOrCreateTable(sourceVo.getTableName())
                  sqlOperationController.selectTable(sourceVo.getTableName())
                  sqlOperationController.saveAllAliasInfo(allPageList)
                  # sqlOperationController.saveAllAliasPriceInfo(allPageList)
                  sqlOperationController.closeLinkSql()
              taskVo1 = {"func":recordDatabase, "param":([onePageData], sourceVo,)}
              spiderCore.getSpiderTaskController().addTaskByType("RECORD_DATABASE", taskVo1)
              print("decode one page data")
              pass
          taskVo = {"func":decodeOnPageDataFunc, "param":(aliasIds, sourceVo,)}
          spiderCore.getSpiderTaskController().addTaskByType("ADD_TASK", taskVo)
      #   # onePageData = sellInfoController.getOnePageAliasPrice(aliasIds, sourceVo)
      #   onePageData = sellInfoController.getOnePageAliasInfo(aliasIds, sourceVo)
      #   allPageList.append(onePageData)
          pageIndex = pageIndex + 1
      else:
          isEnd = True

# print(urlPool.getLen(),urlPool.getUrlVo().getParam())

# if len(allPageList)>0:
#     # 链接数据库
#     sqlOperationController.connectSql()
#     # 判断数据库是否存在
#     sqlOperationController.checkOrCreateTable(sourceVo.getTableName())
#     sqlOperationController.selectTable(sourceVo.getTableName())
#     sqlOperationController.saveAllAliasInfo(allPageList)
#     # sqlOperationController.saveAllAliasPriceInfo(allPageList)
#     sqlOperationController.closeLinkSql()
#     pass

print("欢乐的时光总是过得特别快，Happy times always had a particularly fast")
