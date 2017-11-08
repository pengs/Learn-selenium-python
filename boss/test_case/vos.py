#!/usr/bin/python
# -*- coding: UTF-8 -*-




from Login import *
from  selenium.webdriver.support.select import Select
from  myunit import *

class test_vos(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url = "https://cctest.uccc.cc:8001/?#/login"


    def test_create_vos(self):
         driver = self.driver
         driver.get(self.base_url)

         # 调用登录函数
         Login().user_login(driver, "tongyi", 123123)

         driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[7]/a").click()
         sleep(1)
         driver.find_element_by_xpath( "//*[@id='app']/div[2]/div[1]/div/div/div/ul/li[7]/ul/li[1]/a").click()
         sleep(1)
         select = Select(driver.find_element_by_xpath("//form/div[8]/div/select"))  # 网关类型
         self.assertNotEqual("1", "0")
         select.select_by_value("1")  # 通过value属性
         sleep(1)

         select1 = Select(driver.find_element_by_xpath("//form/div[9]/div/select"))  # 是否开启主叫号码前缀
         self.assertEqual(0, 0)
         select1.select_by_index(0)  # 通过选项的顺序，第一个为 0
         sleep(1)

         select2 = Select(driver.find_element_by_xpath("//form/div[10]/div/select"))  # 手机区号设置
         self.assertIn("开启", "开启（截取号码3位区号：例如596）")
         select2.select_by_visible_text("开启（截取号码3位区号：例如596）")  # 通过选项可见文本


         #调用退出函数
         Login().user_logout(driver)

    def tearDown(self):
         self.driver.quit()


if __name__=="__main__":
    unittest.main()

