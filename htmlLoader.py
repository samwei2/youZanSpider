#coding=utf-8
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
# from youZan.youZanWebBaseConfig import YouZanWebBaseConfig

from bs4 import BeautifulSoup
import js2xml
import sys

class HtmlLoader():
    
    __url = ""
    __headers = {}

    def __init__(self, headers):
        __headers = headers
        print(sys.path)
        return

    def loadHtml(self, url):
        __url = url
        driver = webdriver.Chrome() 


        driver.get(__url)

        htmlText = driver.page_source

        soup = BeautifulSoup(htmlText,"html.parser")

      
        return soup

bb = HtmlLoader({})
# aa = YouZanWebBaseConfig()
# print(aa.getUrlByPage(1))
# import sys
# print(sys.path)
# htmlLoader = HtmlLoader({})
# url = "https://h5.youzan.com/v2/showcase/feature?alias=cug860p2&dc_ps=194209&redirect_count=1"
# soup = htmlLoader.loadHtml(url)
# print(type(soup))
# print(soup)
