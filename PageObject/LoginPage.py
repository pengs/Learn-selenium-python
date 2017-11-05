#!/usr/bin/python
# -*- coding: UTF-8 -*-


from BasePage import *
from selenium.webdriver.common.by import By



class LoginPage():

    '''
    Boss登录页面
    '''

    url='/'

#定位器
    username_loc=(By.XPATH,'//form/div[1]/input')
    password_loc=(By.XPATH,'//form/div[2]/input')
    button_loc=(By.XPATH,'//form/button')

    #具体定位方法
    def login_username(self,username): #输入用户名
        self.find_element(*self.username_loc).send_keys(username)

    def login_password(self,password): #输入密码
        self.find_element(*self.password_loc).send_keys(password)

    def login_button(self): #点击登录按钮
        self.find_element(*self.button_loc).click()

    # def loginout(self):  #退出登录
    #      self.find_element(*self.logout_loc).click()
    #      self.find_element(*self.logout1_loc).click()


    def test_user_login(driver,username,password):
        login_page=LoginPage(driver)
        login_page.open()

        login_page.login_username(username)
        login_page.login_password(password)
        login_page.login_button()








