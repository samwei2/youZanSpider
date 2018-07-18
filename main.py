# coding=utf-8
from allGoodsList import GoodListController
from aliasSellInfo import SellInfoController
from mySqlController import SqlOperationController
import pymysql.cursors
import json

# 全局头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE"
}

# 请求头
f = open('foo.txt')
cookies = {}
for line in f.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value

# print cookies

# 商品控制
goodListController = GoodListController(headers)

sellInfoController = SellInfoController(headers, cookies)

sqlOperationController = SqlOperationController()

# 商品道具列表
aliasIds = goodListController.openGoodsUrl(
    "https://h5.youzan.com/v2/allgoods/16975645?reft=1531274513986&spm=f70430959")  # 拿到当前页所有的商品信息列表

# 保存商品销售数据
aliasTitleDic = {}  # 商品名称字典
sellInfoDic = {}  # 订单信息字典
sellTotalDic = {}  # 产品销量字典
# index = 0
# oneAlias = aliasIds[3]
for oneAlias in aliasIds:
    id = oneAlias[u'alias']
    title = oneAlias[u'title']
    pageArr, total = sellInfoController.checkAliasInfo(id, title)  # 单个商品 购买的详细信息
    aliasTitleDic[id] = title
    sellInfoDic[id] = pageArr
    sellTotalDic[id] = total
pass

print(" goods parser completed, ready connectSql....................")

# 链接数据库
sqlOperationController.connectSql()

sqlOperationController.createTable()

sqlOperationController.saveAliasInfo(aliasTitleDic, sellInfoDic, sellTotalDic)

sqlOperationController.closeLinkSql()
