#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Base import *
from selenium.webdriver.common.by import By


class Loginpage():

    url='/'

    #定位器
    username_loc=(By.XPATH,'//form/div[1]/input')
    password_loc=(By.XPATH,'//form/div[2]/input')
    submit_loc=(By.XPATH,'//form/button')

    #具体定位方法
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()


    def test_user_login(driver,username,password):
        login_page=Loginpage(driver)
        login_page.open()

        login_page.type_username(username)
        login_page.type_password(password)
        login_page.type_submit()







