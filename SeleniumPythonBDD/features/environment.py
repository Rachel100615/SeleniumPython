#coding=utf-8
from selenium import webdriver

def before_all(context): #超级全局变量
    context.driver=webdriver.Chrome()

def after_all(context):
    context.driver.close()