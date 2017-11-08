#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''主要封装用例执行之前需要进行的操作'''

import unittest
from selenium import webdriver

class Mytest(): #定义一个测试类
    global Browser

    def setUp(self):  #初始化数据
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


