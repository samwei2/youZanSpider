# -*- coding: UTF-8 -*-
import pymysql.cursors


class SqlOperationController():
    """docstring for sqlOperation"""
    __cursor = None
    __selectTableName = ""
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
    def createTable(self, tableName):
        self.__cursor = self.__connect.cursor()
        sql_create = '''
           CREATE TABLE `%s` (
              `id` int(255) unsigned NOT NULL AUTO_INCREMENT,
              `aliasId` varchar(255) DEFAULT NULL,
              `buyer` varchar(255) DEFAULT NULL,
              `time` varchar(255) DEFAULT NULL,
              `buyCount` int(255) DEFAULT NULL,
              `price` decimal(8,2) DEFAULT NULL,
              `title` varchar(255) DEFAULT NULL,
              `link` varchar(255) DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=208 DEFAULT CHARSET=utf8;
        '''
        data = (tableName)
        self.__cursor.execute(sql_create % data)
        self.__connect.commit()
        print("dataBase table create completed:", tableName)
    pass

    # 存储所有订单信息
    def saveAllAliasInfo(self, allPageList):
        for onePageData in allPageList:
            # sellInfoDic = onePageData['sellInfoDic']
            self.saveAliasInfo(onePageData)
            pass
        pass

    def saveAliasInfo(self, onePageData):
        # 获取游标
        self.__cursor = self.__connect.cursor()
        index = 0
        for oneAliasObj in onePageData:
            orderArr = oneAliasObj["aliasList"]
            title    = oneAliasObj['title']  # .decode('unicode_escape')
            link     = oneAliasObj['link'] 
            for order in orderArr:
                # print(order)
                dealUid  = order['uid']
                orderData = order['data']
                sql = "INSERT INTO "+self.__selectTableName+" (aliasId, time, buyCount, buyer, title, price, link) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                data = (dealUid, orderData[u'update_time'], orderData[u'item_num'], orderData[u'nickname'], title, orderData[u'item_price'], link)
                insertCode = self.sqlInsert(data, sql, self.__selectTableName, "aliasId")
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
                    print('insert code:', insertCode)
                    pass
                pass
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
                print('insert code:', insertCode)
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

    # 判断是否存在数据库表
    def isHasTable(self, tableName):
        self.__cursor = self.__connect.cursor()
        bHasData = False
        try:
            sql = "SELECT table_name FROM information_schema.TABLES WHERE table_name ='%s'; "
            data = (tableName)
            self.__cursor.execute(sql % data)
            self.__connect.commit()
            bHasData = len(self.__cursor.fetchall()) > 0
            pass
        except Exception as e:
            print("error", tableName + " has not CREATE")
            pass
        return bHasData

    # 查询并创建数据表
    def checkOrCreateTable(self, tableName):
        bHasTable = self.isHasTable( tableName )
        print(bHasTable)
        if bHasTable is False:
            self.createTable(tableName)
            pass
        pass

    # 设置要链接的表名
    def selectTable(self, tableName):
        self.__selectTableName = tableName
        pass

# aa = SqlOperationController()
# aa.connectSql()
# aa.checkOrCreateTable("alias_chaping")