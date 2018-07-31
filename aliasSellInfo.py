#coding=utf-8
import requests
import re
import json
import cookieTool
import urllib2

class SellInfoController():
    """docstring for SellInfoController"""
    __urlPath = "https://h5.youzan.com/v2/trade/order/orderitemlist.json?perpage=10&alias="
    __goodsId = "2ou1uu4wfyybx"
    __pageTab = "&page="
    __page = 1
    __pageArr = [] #当前商品订单数据总和
    __total = 0
    __has_next = True
    __cookies = None

    def __init__(self, headers):
        self.__headers = headers
        self.initData()
        return
        
    def initData(self):

        return

    # 获取单个商品的所有订单详情
    def checkAliasInfo(self, aliasId, aliasTitle, allOrOne=1):
        self.__goodsId = aliasId
        self.__page = 1 #从第一页开始抓数据
        self.__pageArr = []
        self.__total = 0
        self.__has_next = True

        url = ""
        while self.__has_next==True:
            url = self.__urlPath + self.__goodsId + self.__pageTab + str(self.__page)
            print("url ready...", url)
            if self.__cookies==None:
                self.__cookies = cookieTool.CookieTool.getInstance().readCookie()
            # resp = requests.get(url, headers=self.__headers, cookies=self.__cookies)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookies))
            response = opener.open(url)
            res = response.read().decode('utf-8')

            print("html ..decodeing")
            try:
                s = json.loads(res)
            except Exception as e:
                print("you must be change cookies file")
                pass
           
            print("html ..decode end")

            dataList = s['data']['list'] 
            if allOrOne!=1:
                self.__has_next = False
            else:
                self.__has_next = s['data']['has_next']
                pass
            
            print("hes_next..", self.__has_next)

            if self.__total==0:
                self.__total = int(s['data']['total'])
                pass

            # print(s)
            # 
            index = 0
            for line in dataList:
                lineData = {}
                # print line
                index = index + 1
                lineData['uid'] = aliasId + "&p"+ str(self.__page) +"&i"+ str(index)
                lineData['data'] = line
                lineData['title'] = aliasTitle #传一个商品名称进来
                self.__pageArr.append(lineData) 
                # print(lineData['uid'])
            pass

            self.__page = self.__page + 1
            if self.__page>100:
                break
        pass

        print(url + "..all data is completed..")
        

        return self.__pageArr, self.__total

    # 取得一页商品的所有订单
    def getOnePageAliasInfo(self, aliasIds, sourceVo):
        onePageAliasInfo = []
        for oneAlias in aliasIds:
            oneAliasInfo = {}
            id = oneAlias[u'alias']
            title = oneAlias[u'title']
            link  = sourceVo.getAliasLink(id)
            pageArr, total= self.checkAliasInfo(id, title, 0)  #单个商品 购买的详细信息
            oneAliasInfo['id'] = id
            oneAliasInfo['aliasList'] = pageArr
            oneAliasInfo['title'] = title
            oneAliasInfo['link'] = link
            onePageAliasInfo.append(oneAliasInfo)
            pass
        return onePageAliasInfo

    # 获取一页商品的价格详情
    def getOnePageAliasPrice(self, aliasIds, sourceVo):
        onePageAliasPrice = []
        for oneAlias in aliasIds:
            oneAliasPrice = {}
            id = oneAlias[u'alias']
            title = oneAlias[u'title']
            link  = sourceVo.getAliasLink(id)
            pageArr, total= self.checkAliasInfo(id, title, 0)  #单个商品 购买的详细信息,这里只拿一次，拿到价格就撤
            oneAliasPrice["id"] = id
            oneAliasPrice["title"] = title
            oneAliasPrice["price"] = oneAlias[u'price']
            oneAliasPrice["total"] = total
            oneAliasPrice["link"] = link
            if len(pageArr)>0:
                oneAliasPrice['the_last_buy'] = pageArr[0]['data'][u'update_time']
            else:
                oneAliasPrice['the_last_buy'] = "无"               
                pass
           
            onePageAliasPrice.append(oneAliasPrice)
            pass
        # print("-------->", onePageAliasPrice)
        return onePageAliasPrice