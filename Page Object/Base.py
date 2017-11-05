#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''公共的封装'''
from selenium import webdriver
from  time import sleep

class Page():

    '''页面基础类，用于页面对象类的继承'''

    def __init__(self,driver):
        '''初始化数据'''
        self.driver = driver
        self.base_url = 'https://cctest.uccc.cc:8001/?#/login'
        self.timeout=10


    def on_page(self):
        '''判断打开的网页是否和预期一致'''
        return  self.driver.current_url==(self.base_url+self.url)

    def _open(self,url):#私有_open方法
         url=self.base_url+url
         print ('Test page is %s'%url)
         self.driver.maximize_window()
         self.driver.get(url)
         assert self.on_page(),'Did not load on %s' %url

    def open(self): #公共open方法
        self._open(self.url)

    def find_element(self,*loc): #定义一个元素定位的方法
        return  self.find_element(*loc)


