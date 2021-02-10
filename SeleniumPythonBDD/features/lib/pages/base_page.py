#coding=utf-8
#抽出所有页面公用的东西
from selenium import webdriver
import traceback
from selenium.webdriver.common.by import By
import time
class BasePage():
    def __init__(self,driver,url="http://www.5itest.cn/register"):
        self.url=url
        self.driver=driver
        self.timeout=20

    def get_url(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(slef,*loc):
        return slef.driver.find_element(*loc)

