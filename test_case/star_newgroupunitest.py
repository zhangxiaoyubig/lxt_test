#coding=utf-8
from selenium import webdriver
import time
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select
import  unittest

class Newgroup(unittest.TestCase):

    def setUp(self):
        self.driver  = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        self.url = "http://wsale.test.4000669696.com/"
        # 填加新集团信息
        self.groupname = u'10.12.6集团'  # 必填
        self.groupaddress = u'北京'  # 必填，集团地址
        self.groupadWebsite = '38822.wgp.test.4000669696.com'  # 必填，集团网址
        self.groupmail = 'www.xiaoyuz.zhang_big@sina.com'  # 必填
        self.grouptel = '136888888888'
        self.groupfax = ''  # 传真
        self.contacts = u'联系人张霄雨'  # 必填，联系人
        self.contactstel = '13271953478'  # 必填，联系人电话
        self.zhifubao = ''
        self.peopleid = ''
        self.zhifubaopassword = ''
        self.branchnumble = ''  # 分支数量
        self.studeltnumble = ''

    def test_newgroup(self):

        u"""增加集团用例"""
        #登录销售地址
        self.driver.get(self.url)
        self.driver.maximize_window()
        beforetitle = self.driver.title
        print u"登录之前的title -->  " + beforetitle
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("13800880088")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("123123")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
        aftertitle = self.driver.title
        print u"现在的title -->  " + aftertitle
        if aftertitle  ==  u"微语言 销售 后台" :
            print u"title验证成功，销售平台登录成功"
        else:
            print u"title验证失败，销售平台登录失败"


        # 点击“销售管理”->“客户列表”
        self.driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div[1]/section[1]/a/button").click()
        print "进入集团编辑页面"

        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[1]/div/input").clear()
        self. driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[1]/div/input").send_keys(self.groupname)
        self. driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[2]/div/input").send_keys(self.groupaddress)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[3]/div/input").send_keys(self.groupadWebsite)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[4]/div/input").send_keys(self.groupmail)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[5]/div/input").send_keys(self.grouptel)
        # driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[6]/div/input").send_keys(groupfax)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[3]/div/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[3]/div/input").send_keys(self.contacts)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[4]/div/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[4]/div/input").send_keys(self.contactstel)

        # 使用execute_script方法来执行js代码
        # 拖到底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(1)
        # 继续输入集团信息
        # 使用Select来进行下拉框操作
        sel = self.driver.find_element_by_xpath(".//*[@id='cooperation_type']")
        # 从0开始
        Select(sel).select_by_value('1')
        # sela = driver.find_element_by_xpath(".//*[@id='bookss']/div[12]/div/select")
        # Select(sela).select_by_value('1')
        sela = self.driver.find_element_by_xpath(".//*[@id='bookss']/div[13]/div/select")
        Select(sela).select_by_value('3')
        print "集团编辑完成"
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[14]/div[1]/button").click()
        print "集团创建成功"
        self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[9]/a[2]/button").click()
        # sel = driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/select")
        # Select(sel).select_by_value('2')
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div[1]/button").click()
        self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[9]/a[3]/button").click()
        print '集团已经分配给运营'

        # 登录运营平台
        self.driver.get("http://woperate.test.4000669696.com")
        beforetitle = self.driver.title
        print u"登录之前的title -->  " + beforetitle
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("13426252525")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("password")
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
        aftertitle = self.driver.title
        print u"现在的title -->  " + aftertitle
        if aftertitle == u"微语言  运营 后台 ":
            print u"title验证成功，运营平台登录成功"
        else:
            print u"title验证失败，运营平台登录失败"
        self.driver.refresh()

        self.driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/a/span").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[11]/a[1]/button").click()
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(1)
        print "进入集团管理员编辑页面"

        admname = u"管gu理"
        admpassd = "123123"
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[16]/div/input").send_keys(admname)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[17]/div/input").send_keys(self.contactstel)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[18]/div/input").send_keys(admpassd)
        self.driver.find_element_by_xpath(".//*[@id='bookss']/div[20]/div[1]/button").click()
        # if判断返回的内容
        print "集团管理员设置成功"
        time.sleep(3)

        # 登录新集团平台
        self.driver.get("http://" + self.groupadWebsite)
        beforetitle = self.driver.title
        print u"登录之前的title -->  " + beforetitle
        self.driver.find_element_by_xpath(".//*[@id='userName1']").send_keys(admname)
        self.driver.find_element_by_xpath(".//*[@id='password']").send_keys(admpassd)
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[3]/a").click()
        aftertitle = self.driver.title
        print u"现在的title -->  " + aftertitle
        if aftertitle == u"  分支 管理后台 ":
            print u"title验证成功，分支平台登录成功"
        else:
            print u"title验证失败，分支平台登录失败"

        # 获得当前的句柄
        # sreach_window = driver.current_window_handle

    def tearDown(self):
        self.driver.quit()

if __name__== "_main_":

    # 构造测试集
    suite = unittest.TestSuite
    suite.addTest(Newgroup("test_newgroup"))
    #执行测试
    runnner = unittest.TextTestRunner
    runnner.run(suite)
