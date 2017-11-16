# coding=utf-8
import unittest
import  HTMLTestRunner
import time
#把test_case 目录添加到path 下，这里用的相对路径
import  sys
sys.path.append("C:\Python27\selenium\webdriver\test_case")
#导入测试文件
from  test_case import  star_addSalespersonunit
from  test_case import  star_searchunitest
from   test_case import  star_newgroupunitest
import allcase_list


#将用例装在数组中
alltestnames = allcase_list.caselist()

#创建测试套件
testunit=unittest.TestSuite()
#循环读取数组中的用例
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))

#定义报告存放地址!!时间有问题bug！！
nowtime = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
filename = "C:\\Python27\\selenium\\webdriver\\report\\"+nowtime+'result.html'
fp = file(filename,'wb')

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'两个用例的运行测试报告',
    description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
