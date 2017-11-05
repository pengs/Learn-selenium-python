# Boss系统自动化测试


 PageObject设计模式是Selenium官网推荐的一种自动化构建模式。
 PageObject设计模式对网页进行一个简单抽象，将每个页面设计成一个类，页面元素定位、元素操作、用户行为都被封装进对应的类。编写测试用例时不再直接操作页面元素，而是调用对应页面类的方法。
 使得测试人员在编写用例时能更多的关注业务逻辑，而不是页面结构与元素。
  * 项目结构介绍：
  * boss/test_case/models
  
    1.function --公用方法（截图/查找对象报告/邮件发送报告）
    
    2.myunit --用例执行前后的准备工作
  
  * boss/runtest 
    --执行测试用例
  
  * boss/HTMLTestRunner_jpg.py 
    --生成测试报告模板
  
  * test_data 
    --测试数据
 
  * test_report
    --测试报告和截图文件夹
     
  * driver
     --浏览器驱动
     
    
  
  
  
  
  
  
  

