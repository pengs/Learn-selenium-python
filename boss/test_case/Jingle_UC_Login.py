#!/usr/bin/python
# -*- coding: UTF-8 -*-
''''数据驱动模型-登录和退出公共测试用例'''


from selenium.webdriver.common.by import By
from time import sleep
from myunit import *

class Jingle_Login(): #定义一个登录类


    def user_login(self,driver,account,password): #定义一个用户登录的方法
         '''登录钉铛UC运营系统'''
         driver.find_element(By.XPATH, "//form/div[1]/input").clear()
         driver.find_element(By.XPATH,"//form/div[1]/input").send_keys(account) #By方法定位
         driver.find_element(By.XPATH, "//form/div[2]/input").clear()
         driver.find_element_by_xpath("//form/div[2]/input").send_keys(password)#直接find_element定位
         driver.find_element(By.XPATH,"//form/button").click()#点击登录
         sleep(2)

    def user_logout(self,driver):
        '''退出登录'''
        driver.find_element(By.XPATH,"/html/body/div/div[2]/nav/div[2]/div[1]/ul[2]/li/a").click()
        sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/nav/div[2]/div[1]/ul[2]/li/ul").click()


if __name__=='__main__':

    '''可以输入多个登录账号'''
    driver = webdriver.Chrome() #调用谷歌浏览器驱动
    driver.implicitly_wait(15) #设置隐式等待
    driver.get("https://jingleapp.uccc.cc/manage/jingle/#/login")

#调用Login类里面的方法
    Jingle_Login().user_login(driver,"test",'TongYitest') #用户和密码
    sleep(2)
    Jingle_Login().user_logout(driver)  #退出登录
    # assertEqual[]
    sleep(3)
#关闭浏览器
    driver.quit()