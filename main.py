#coding=utf-8
from allGoodsList import GoodListController
from aliasSellInfo import SellInfoController
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

#商品道具列表
aliasIds = {}
aliasIds['id'], aliasIds['title'] = goodListController.openGoodsUrl("https://h5.youzan.com/v2/allgoods/16975645?reft=1531274513986&spm=f70430959")

# 单页商品数目
print(len(aliasIds['id']))

#保存商品销售数据
dic = {}
dicKey = {}
index = 0
for id in aliasIds['id']:
	dicKey[index] = {}
	dic[index], dicKey[index]['total'] = sellInfoController.checkAliasInfo(id)  #单个商品 购买的详细信息
	dicKey[index]['id'] = id
	dicKey[index]['title'] = aliasIds['title'][index] #id 和 title 的索引是一致的
	print(dicKey[index]['title'],"==============>",id, dicKey[index]['total'])
	index = index+1
pass




# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    db='alias',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# dicKeyData = dicKey[1]
# dicData = dic[1][0]

# print(type(dicData))
# print(dicData[u'update_time'])
index = 0
for a in dic:
	# 一件商品的数据
	indexData = dic[a]
	# print(a, indexData)
	for b in indexData:
		# 详细信息
		infoData = b
		titleData = dicKey[a]
		fff = float(infoData[u'item_price'])
		# print( type(infoData[u'item_price']) , fff, type(fff) )
		# 插入数据
		sql = "INSERT INTO aliasInfo (buyer, time, buyCount, aliasId, price, title) VALUES ('%s', '%s', '%s', '%.2f', '%s')"
		data = (infoData[u'nickname'], infoData[u'update_time'], infoData[u'item_num'], titleData['id'], fff, (titleData[u'title']).decode('unicode_escape'))
		cursor.execute(sql % data)
		connect.commit()
		index = index+1
		if index>8:
			index = 0
			pass
		str = ""

		for x in xrange(1,index):
			str = str + "........................."
			pass

		print('成功插入'+str)
		pass
	pass

print('成功插入')#, cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
connect.close()
