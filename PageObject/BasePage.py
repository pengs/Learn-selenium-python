#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''公共的封装'''


from selenium import webdriver
from time import sleep

class Page():

    '''页面基础类，用于页面对象类的继承'''



    def __init__(self,driver): #初始化参数（驱动，URL地址，超时时长）
        '''初始化数据'''
        self.driver = driver
        self.base_url = 'https://cctest.uccc.cc:8001/?#/login'
        self.timeout=10

    def _open(self,url):#私有_open方法
         url=self.base_url+url
         print ('Test page is %s'%url)
         self.driver.maximize_window()
         self.driver.get(url)
         assert self.on_page(),'Did not load on %s' %url

    def open(self):  # 打开地址
        self._open(self.url)

    def on_page(self):
        '''判断打开的网页是否和预期一致'''
        return self.driver.current_url == (self.base_url + self.url)


    def find_element(self,*loc): #定义一个元素定位的方法
        return self.driver.find_element(*loc)

    def find_elements(self,*loc): #定位多个元素
        return self.driver.find_elements(*loc)


