# coding=utf-8
from selenium import webdriver
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select
import  unittest

class addSaleper(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        self.url = "http://wsale.test.4000669696.com/"
        self.personname = u"销售1"  # 销售姓名
        self.personpassword = "123123"  # 销售密码
        self.persontel = "13683552243"  # 联系方式

    def test_addSalesperson(self):
        u'''增加销售人员用例'''
        self.driver.get(self.url)
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("13800880088")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("123123")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
        print "销售平台登录成功"

        self.driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div[1]/section[1]/a/button").click()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/input").send_keys(self.personname)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div/input").send_keys(self.personpassword)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[3]/div/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[3]/div/input").send_keys(self.persontel)

        position = self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[4]/div/select")  # 职位
        Select(position).select_by_value('2')
        Gender = self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[4]/div/select")  # 性别
        Select(Gender).select_by_value('2')

        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[6]/div[1]/button").click()
        # 获取元素内容
        na = self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[1]").text
        if na == self.personname:
            print "销售账号添加成功"
        else:
            print "账号添加失败，请查看"

        # 验证是否为开启状态，如果不是就点击开启
        go = self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[6]/a[2]/button").text
        if go == "开启":
            print "现在为开启状态"
        else:
            self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[6]/a[2]/button").click()
            print "开启成功"

    def tearDown(self):
            self.driver.quit()

if __name__== "_main_":

    # 构造测试集
    suite = unittest.TestSuite
    suite.addTest(addSaleper("test_sale"))

    #执行测试
    runnner = unittest.TextTestRunner
    runnner.run(suite)


