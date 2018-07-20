# -*- coding: UTF-8 -*-
import pymysql.cursors


class SqlOperationController():
    """docstring for sqlOperation"""
    __cursor = None
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

    # 存储所有订单信息
    def saveAllAliasInfo(self, allPageList):
        for onePageData in allPageList:
            sellInfoDic = onePageData['sellInfoDic']
            self.saveAliasInfo(sellInfoDic)
            pass
        pass

    def saveAliasInfo(self, sellInfoDic):
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

    # 存储所有商品价格
    def saveAllAliasPriceInfo(self, allPageList):
        # print(allPageList)
        for onePageData in allPageList:
            self.saveAliasPrice(onePageData)
            pass
        pass

    #单页的商品价格保存
    def saveAliasPrice(self, onePageData):
        # 获取游标
        self.__cursor = self.__connect.cursor()
        index = 0
        for oneAlias in onePageData:
            aliasId = oneAlias['id']
            sql = "INSERT INTO alias_price (aliasId, title, price, total, link, the_last_buy) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
            data = (aliasId, oneAlias['title'], oneAlias['price'], oneAlias['total'], oneAlias['link'], oneAlias['the_last_buy'])
            insertCode = self.sqlInsert(data, sql, "alias_price", "aliasId")

            if insertCode==0:
                index = index + 1
                if index > 8:
                    index = 0
                    pass

                str = ""
                for x in xrange(1, index):
                    str = str + "..."
                    pass

                print('成功插入' + str)
            else:
                index = 0
                print('插入失败 code:', insertCode)
                pass
            pass
        pass


    # 插入数据 data:要插入的数据,   sql:sql 语句
    def sqlInsert(self, data, sql, tableName, tableKey):
        code = 0
        bHasData = False
        try:
            selectSql = "SELECT " + tableKey + " FROM "+ tableName + " WHERE " + tableKey + " = '%s'"
            uidData = data[0]
            # print(selectSql, uidData)
            self.__cursor.execute(selectSql % uidData)
            bHasData = len(self.__cursor.fetchall()) > 0
            pass
        except Exception as e:
            print("SELECT error", e.message, selectSql)
            code = 1
            pass

        if bHasData is False:
            try:
                # 插入数据
                # sql = "INSERT INTO aliasInfo (buyer, time, buyCount, aliasId, title, price) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
                self.__cursor.execute(sql % data)
                self.__connect.commit()
                pass
            except Exception as e:
                code = 2
                print("INSERT error", e.message)
                print("sql not data ,we will write in ....")
                pass
        else:
            print("data is has , we will updata...")
            code = 3
            # sql = "UPDATE aliasInfo  set buyer = '%s'"
            # self.__cursor.execute(sql % ("aaa"))
            # self.__connect.commit()
            pass
     
        return code
        pass


    # 关闭连接
    def closeLinkSql(self):
        try:
            if  self.__cursor:
                self.__cursor.close()
                pass
            
            self.__connect.close()
            pass
        except Exception as e:
            print("closeLinkSql error", e.message)
            pass
        pass
