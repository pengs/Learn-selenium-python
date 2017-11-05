#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''创建一个截图功能函数，方便调用，同时也采用相对路径的方法将测试截图保存到对应的目录下'''

from  selenium import  webdriver
import os

#创建截图函数

def insert_img(driver,filename): #截图函数

  base_dir=os.path.dirname(os.path.dirname(__file__)) #获取目标文件路径
  base_dir=str(base_dir)   #转换成字符串
  base_dir=base_dir.replace('\\','/')   #将绝对路径转换成相对路径
  base=base_dir.split('/boss')[0] #切割成列表取值
  filepath=base+"/boss/test_report/screenshot_"+filename #拼接路径，相对路径引用
  driver.get_screenshot_as_file(filepath) #保存到对应的文件下



if __name__=='__main__':
    driver= webdriver.Chrome()
    driver.get("https://cctest.uccc.cc:8001/?#/login")
    insert_img(driver,'boss.jpg')
    driver.quit()