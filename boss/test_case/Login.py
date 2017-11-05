#!/usr/bin/python
# -*- coding: UTF-8 -*-
''''数据驱动模型-登录公共测试用例'''


from selenium import webdriver
from time import sleep

class Login(): #定义一个登录类


    def user_login(self,driver,account,password): #定义一个用户登录的方法
         '''UC运营系统登录'''
         driver.find_element_by_xpath("//form/div[1]/input").send_keys(account)
         driver.find_element_by_xpath("//form/div[2]/input").send_keys(password)
         driver.find_element_by_xpath("//form/button").click() #点击登录
         sleep(1)



    def user_logout(self,driver):
        '''UC运营系统退出登录'''
        driver.find_element_by_xpath("//*[@id='site-navbar-collapse']/ul[2]/li[2]/a").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='site-navbar-collapse']/ul[2]/li[2]/ul/li[4]/a").click()


if __name__=='__main__':

    '''可以输入多个登录账号'''
    driver = webdriver.Chrome() #调用谷歌浏览器驱动
    driver.get("https://cctest.uccc.cc:8001/?#/login") #请求访问的地址

#调用Login类里面的方法
    Login().user_login(driver,"tongyi",123123) #用户和密码
    sleep(2)
    Login().user_logout(driver)  #退出登录
    sleep(3)
#关闭浏览器
    driver.quit()