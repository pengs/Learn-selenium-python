#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''浏览器驱动'''

from  selenium import  webdriver
import time

#启动浏览器驱动
def browser(): #浏览器驱动函数

    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()

    return driver

if __name__=='__main__':

    browser()
