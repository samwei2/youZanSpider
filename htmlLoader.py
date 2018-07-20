#coding=utf-8
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

from bs4 import BeautifulSoup
import js2xml
import sys

class HtmlLoader():
    
    __url = ""
    __headers = {}

    def __init__(self, headers):
        self.__headers = headers
        return

    def loadHtml(self, url):
        self.__url = url
        driver = webdriver.Chrome() 


        driver.get(self.__url)
        print("webdriver get url--->", self.__url)

        htmlText = driver.page_source

        soup = BeautifulSoup(htmlText,"html.parser")
      
        driver.quit()
        return soup


# aa = HtmlLoader({})
# print(aa.loadHtml("https://h5.youzan.com/v2/showcase/goods/allgoods?kdt_id=15311495&p=7"))