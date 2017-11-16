# coding=utf-8
from selenium import webdriver
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select
import unittest
#引入测试报告
import  HTMLTestRunner
class Sale(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        self.url = "http://wsale.test.4000669696.com/"
        self.personname = u"销售1"  # 销售姓名
        self.personpassword = "123123"  # 销售密码
        self.persontel = "13683552243"  # 联系方式

    def test_sale(self):
        u"""销售分配用例"""
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("13800880088")
        driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("123123")
        driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
        print "销售平台登录成功"

        # driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/a/span").click()
        driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a").click()
        # 搜索条件。1.集团名称2.销售负责人
        tiaojian = driver.find_element_by_xpath(
            "html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[1]/select")
        Select(tiaojian).select_by_value('2')
        # 不确定要填什么
        driver.find_element_by_xpath(
            "html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[2]/input").send_keys(u"不知道填什么")
        # 来源情况。1.来源情况（全部）2.在线注册3.系统注册
        laiyuan = driver.find_element_by_xpath(
            "html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[3]/select")
        Select(laiyuan).select_by_value('2')
        # 分配情况。1.未分配2.已分配
        fenpei = driver.find_element_by_xpath(
            "html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[4]/select")
        Select(fenpei).select_by_value('2')
        # 合作关系。1.战略合作2.普通合作
        hezuo = driver.find_element_by_xpath(".//*[@id='cooperation_type']")
        Select(hezuo).select_by_value('2')
        # driver.find_element_by_xpath(".//*[@id='search-btn']").click()
        print"搜索完成"


    def tearDown(self):
            self.driver.quit()

if __name__== "_main_":

    # 构造测试集
    suite = unittest.TestSuite
    suite.addTest(Sale("test_sale"))

    #执行测试
    runnner = unittest.TextTestRunner
    runnner.run(suite)




