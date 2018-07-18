# coding=utf-8
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

from bs4 import BeautifulSoup


class GoodListController():
    __url = ""
    __headers = {}

    def __init__(self, headers):
        __headers = headers
        return

    def openGoodsUrl(self, url):
        __url = url
        driver = webdriver.Chrome()

        driver.get(__url)

        htmlText = driver.page_source

        soup = BeautifulSoup(htmlText, "html.parser")

        script = soup.body.script

        lala = re.findall(r'var _showcase_components =\s+((.*?])+)', script.string)

        if lala:
            tt = lala[0][0].decode('utf-8')
            # print(type(lala[0][0]))

            hh = json.loads(tt)
            # print(hh[0],type(hh[0]))
            goods = hh[0][u'goods']  # 当前页中所有的道具信息

        # for x in goods:
        # 	print("\r\n")
        # 	print(x[u'alias'], x[u'title'])
        # pass

        # sou = re.findall(r'\"alias\":\"(\w+)', script.string)
        # sou = self.delRepetition(sou)
        # title = re.findall(r'\"title":\"(.+?)\"', script.string)
        # title = self.delRepetition(title)

        # for x in sou:
        # 	print x
        # pass

        # for x in title:
        # 	print x.decode('unicode_escape')
        # 	pass

        driver.quit()
        return goods

    # 去掉数组重复的项，并保留原来的顺序
    def delRepetition(self, arr):
        newArr = []
        for x in arr:
            if x not in newArr:
                newArr.append(x)
        pass
        return newArr

# url = "https://h5.youzan.com/v2/allgoods/16975645?reft=1531274513986&spm=f70430959"
