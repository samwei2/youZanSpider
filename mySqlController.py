# -*- coding: UTF-8 -*-
import pymysql.cursors


class SqlOperationController():
    """docstring for sqlOperation"""

    def __init__(self):
        pass

    def connectSql(self):
        # 连接数据库
        self.__connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='',
            db='alias',
            charset='utf8'
        )
        pass

    # 创建表
    def createTable(self):
        self.__cursor = self.__connect.cursor()
        sql_create = '''
            CREATE TABLE `aliasinfo` (
              `id` int(255) unsigned NOT NULL AUTO_INCREMENT,
              `buyer` varchar(255) DEFAULT NULL,
              `time` varchar(255) DEFAULT NULL,
              `buyCount` int(255) DEFAULT NULL,
              `aliasId` varchar(255) DEFAULT NULL,
              `price` decimal(8,2) DEFAULT NULL,
              `title` varchar(255) DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=963 DEFAULT CHARSET=utf8;
        '''
        self.__cursor.execute(sql_create)
        self.__connect.commit()
    pass


    def saveAliasInfo(self, aliasTitleDic, sellInfoDic, sellTotalDic):
        # 获取游标
        self.__cursor = self.__connect.cursor()
        index = 0

        for key in sellInfoDic:
            # print(sellInfoDic[key])
            # # 一件商品的数据
            sellInfoList = sellInfoDic[key]
            if sellInfoList is None or len(sellInfoList) == 0:
                continue

            for sellInfo in sellInfoList:
                infoData = sellInfo['data']
                dealUid = sellInfo['uid']
                title = sellInfo['title']  # .decode('unicode_escape')
                data = (infoData[u'nickname'], infoData[u'update_time'], infoData[u'item_num'], dealUid, title,
                        infoData[u'item_price'])
                # print("ready write data", data)
                # print(dealUid, "is ready write to sql")

                bHasData = False
                try:
                    sql = "SELECT aliasId FROM aliasInfo WHERE aliasId = '%s'"
                    uidData = (dealUid)
                    self.__cursor.execute(sql % uidData)
                    bHasData = len(self.__cursor.fetchall()) > 0
                    pass
                except Exception as e:
                    print("SELECT error", e.message)
                    pass

                if bHasData is False:
                    try:
                        # 插入数据
                        sql = "INSERT INTO aliasInfo (buyer, time, buyCount, aliasId, title, price) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
                        self.__cursor.execute(sql % data)
                        self.__connect.commit()

                        index = index + 1
                        if index > 8:
                            index = 0
                            pass
                        str = ""

                        for x in xrange(1, index):
                            str = str + "..."
                            pass

                        print('成功插入' + str)
                        pass
                    except Exception as e:
                        print("INSERT error", e.message)
                        pass
                        print("sql not data ,we will write in ....")
                    pass
                else:
                    print("data is has , we will updata...")
                # sql = "UPDATE aliasInfo  set buyer = '%s'"
                # self.__cursor.execute(sql % ("aaa"))
                # self.__connect.commit()
                pass

            print('录入结束')
        pass


    # 关闭连接
    def closeLinkSql(self):
        self.__cursor.close()
        self.__connect.close()
        pass

    # indexData = dic[a]
    # 	# dealUid = dic[a]
    # 	# print("================================>", dic[a])
    # 	# print(a, indexData)
    # 	for b in indexData:
    # 		# 详细信息
    # 		infoData = b['data']
    # 		dealUid  = b['uid']
    # 		titleData = dicKey[a]

    # 		#查找数据
    # 		try:
    # 			sql = ""
    # 			pass
    # 		except Exception as e:
    # 			print(e.message)
    # 			pass

    # 		# 插入数据
    # 		try:
    # 			sql = "INSERT INTO aliasInfo (buyer, time, buyCount, aliasId, title, price) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
    # 			data = (infoData[u'nickname'], infoData[u'update_time'], infoData[u'item_num'], dealUid, (titleData[u'title']).decode('unicode_escape'), infoData[u'item_price'])
    # 			self.__cursor.execute(sql % data)
    # 			self.__connect.commit()
    # 			pass
    # 		except Exception as e:
    # 			print(e.message)
    # 			pass

    # 		index = index+1
    # 		if index>8:
    # 			index = 0
    # 			pass
    # 		str = ""

    # 		for x in xrange(1,index):
    # 			str = str + "..."
    # 			pass

    # 		print('成功插入'+str)
    # 		pass
    # 	pass
