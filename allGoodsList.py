#coding=utf-8
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from htmlLoader import HtmlLoader
from bs4 import BeautifulSoup
import js2xml

class GoodListController():
    
    __url = ""
    __headers = {}


    def __init__(self, headers):
        self.__headers = headers
        self.__htmlLoader = HtmlLoader(self.__headers)
        return

    def openGoodsUrl(self, url):
        self.__url = url
        soup = self.__htmlLoader.loadHtml(self.__url)
        script = soup.body.script

        lala = re.findall(r'var _showcase_components =\s+((.*?])+)', script.string)

        if lala:
            tt = lala[0][0].decode('utf-8')
            hh = json.loads(tt)
            goods = hh[0][u'goods'] #当前页中所有的道具信息

        return goods