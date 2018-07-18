#coding=utf-8
from allGoodsList import GoodListController
from aliasSellInfo import SellInfoController
from mySqlController import SqlOperationController
import pymysql.cursors
import json

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
beginPage = 1
endPage = 49

for page in range(1,49):
    url = "https://h5.youzan.com/v2/showcase/goods/allgoods?kdt_id=16975645&p=" + str(page)
    aliasIds = goodListController.openGoodsUrl(url) #拿到当前页所有的商品信息列表
    #保存商品销售数据
    aliasTitleDic = {} # 商品名称字典
    sellInfoDic = {}  # 订单信息字典
    sellTotalDic = {}  # 产品销量字典
    for oneAlias in aliasIds:
        id = oneAlias[u'alias']
        title = oneAlias[u'title']
        pageArr, total= sellInfoController.checkAliasInfo(id, title)  #单个商品 购买的详细信息
        aliasTitleDic[id] = title
        sellInfoDic[id] = pageArr
        sellTotalDic[id] = total
    pass

    onePageData = {}
    onePageData['aliasTitleDic'] = aliasTitleDic
    onePageData['sellInfoDic'] = sellInfoDic
    onePageData['sellTotalDic'] = sellTotalDic

    allPageList.append(onePageData)
    pass

# 链接数据库
sqlOperationController.connectSql()

# 没有数据库的话可以打开这条
# sqlOperationController.createTable()

for onePageData in allPageList:
    aliasTitleDic = onePageData['aliasTitleDic']
    sellInfoDic = onePageData['sellInfoDic']
    sellTotalDic = onePageData['sellTotalDic'] 
    sqlOperationController.saveAliasInfo(aliasTitleDic, sellInfoDic, sellTotalDic)
    pass

sqlOperationController.closeLinkSql()