#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import HTMLTestRunner_jpg
import time

#python2.7要是报编码问题，就加这三行，python3不用加
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 定义测试用例路径
test_dir='./test_case'

#存放报告的文件夹
report_dir='./test_report'

#报告命令时间格式
now =time.strftime("%Y-%m-%d %H-%M-%S" )

#报告完整路径
report_name=report_dir+'/'+now+'result.html'

if __name__ == "__main__":
   #批量执行测试用例
   discover = unittest.defaultTestLoader.discover(test_dir, pattern="Boss*.py")
   run = HTMLTestRunner_jpg.HTMLTestRunner(title="测试报告",
                                              description="测试用例",
                                              stream=open(report_name, "wb"),
                                              verbosity=2,
                                              retry=1)

   run.run(discover)
