#coding=utf-8
import cookielib
import urllib2
class CookieTool:
    __cookieFilePath = 'cookie/cookie.txt'
    __instance = None
    @classmethod  # 调用类的方法来创建一个单例
    def getInstance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = CookieTool()
            return cls.__instance

    def __init__(self):
        self.initializeTool()

    def initializeTool(self):
        #设置保存cookie的文件，同级目录下的cookie.txt
        self.filename = self.__cookieFilePath
        #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        self.cookie = cookielib.MozillaCookieJar(self.filename)
        #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        #通过handler来构建opener
        self.opener = urllib2.build_opener(self.handler)

    def saveUrlCookie(self, url):
        #创建一个请求，原理同urllib2的urlopen
        self.response = self.opener.open(url)
        #保存cookie到文件
        self.cookie.save(ignore_discard=True, ignore_expires=True)

    def readCookie(self):
        #创建MozillaCookieJar实例对象
        self.cookieRead = cookielib.MozillaCookieJar()
        #从文件中读取cookie内容到变量
        self.cookieRead.load(self.__cookieFilePath, ignore_discard=True, ignore_expires=True)
        return self.cookieRead
# import cookielib
# import urllib2
# import json
#
# aa = CookieTool()
# aa.saveUrlCookie('https://h5.youzan.com/v2/showcase/goods/allgoods?kdt_id=16975645&p=1')
# # #创建请求的request
# req = urllib2.Request("https://h5.youzan.com/v2/trade/order/orderitemlist.json?perpage=10&alias=2fxs6gs7juqn1&page=1")
# cookie = aa.readCookie()
# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print(response.read())
# res =  response.read().decode('utf-8')
# try:
#     s = json.loads(res)
# except Exception as e:
#     print("you must be change cookies file")
#     pass
#
# print("html ..decode end")
#
# dataList = s['data']['list']
# print(dataList)