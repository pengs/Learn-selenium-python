#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''主要封装用例执行之前需要进行的操作'''

import unittest

from driver.driver import *


class Mytest(unittest.TestCase): #定义一个测试类

    def setUp(self):  #初始化数据
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()





