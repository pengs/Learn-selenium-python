#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 11:35
# @Author  : dapengchiji！！
# @FileName: JIngle_Manage_Login.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
''''数据驱动模型-登录和退出公共测试用例'''


from selenium.webdriver.common.by import By
from time import sleep
from myunit import *

class Jingle_Manage_Login(): #定义一个登录类


    def user_login(self,driver,account,password): #定义一个用户登录的方法
         '''登录钉铛管理系统'''
         driver.find_element_by_xpath('//*[@id="viewport"]/nav/div/button[1]' ).click()
         driver.find_element(By.XPATH, '//*[@id="viewport"]/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
         driver.find_element(By.XPATH, '//*[@id="viewport"]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(account) #By方法定位
         sleep(0.5)
         driver.find_element(By.XPATH, '//*[@id="viewport"]/div[3]/div/div[2]/form/div[2]/div/div/input').clear()
         driver.find_element_by_xpath('//*[@id="viewport"]/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys(password)#直接find_element定位
         sleep(0.5)
         driver.find_element(By.XPATH,'//*[@id="viewport"]/div[3]/div/div[2]/div[2]/button').click()#点击登录
         sleep(1)

    def user_logout(self,driver):
        '''退出登录'''
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav/div[3]/div/button[3]").click()
        sleep(1)


if __name__=='__main__':

    '''可以输入多个登录账号'''
    driver = webdriver.Chrome() #调用谷歌浏览器驱动
    driver.implicitly_wait(15) #设置隐式等待
    driver.get("https://jingleapp.uccc.cc/jingle/login.html#/intro/index")
    sleep(1)
#调用Login类里面的方法
    Jingle_Manage_Login().user_login(driver,"18600198272",'qwe123') #用户和密码
    sleep(2)
    Jingle_Manage_Login().user_logout(driver)  #退出登录
    # assertEqual[]
    sleep(2)
#关闭浏览器
    driver.quit()

