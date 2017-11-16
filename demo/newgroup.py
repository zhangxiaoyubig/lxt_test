#coding=utf-8
from selenium import webdriver
import time
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

def salelogin(username,password):

    driver.get("http://wsale.test.4000669696.com/")
    driver.maximize_window()
    beforetitle = driver.title
    print u"登录之前的title -->  " + beforetitle
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys(username )
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    aftertitle = driver.title
    print u"现在的title -->  " + aftertitle
    if aftertitle  ==  u"微语言 销售 后台" :
        print u"title验证成功，销售平台登录成功"
    else:
        print u"title验证失败，销售平台登录失败"

#销售首页模块登录
salelogin("15011420126", "123123")

# 点击“销售管理”->“客户列表”
driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a").click()
driver.find_element_by_xpath("html/body/div[1]/div[1]/section[1]/a/button").click()
print "进入集团编辑页面"

# 填加新集团信息
groupname = u'10.12.6集团'  # 必填
groupaddress = u'北京'  # 必填，集团地址
groupadWebsite = '38822.wgp.test.4000669696.com'  # 必填，集团网址
groupmail = 'www.xiaoyuz.zhang_big@sina.com'  # 必填
grouptel = '136888888888'
groupfax = ''  # 传真
contacts = u'联系人张霄雨'  # 必填，联系人
contactstel = '13271953478'  # 必填，联系人电话
zhifubao = ''
peopleid = ''
zhifubaopassword = ''
branchnumble = ''  # 分支数量
studeltnumble = ''

driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[1]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[1]/div/input").send_keys(groupname)
driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[2]/div/input").send_keys(groupaddress)
driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[3]/div/input").send_keys(groupadWebsite)
driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[4]/div/input").send_keys(groupmail)
driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[5]/div/input").send_keys(grouptel)
# driver.find_element_by_xpath(".//*[@id='bookss']/div[1]/div[6]/div/input").send_keys(groupfax)
driver.find_element_by_xpath(".//*[@id='bookss']/div[3]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div[3]/div/input").send_keys(contacts)
driver.find_element_by_xpath(".//*[@id='bookss']/div[4]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div[4]/div/input").send_keys(contactstel)

# 使用execute_script方法来执行js代码
# 拖到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(1)
# 继续输入集团信息
# 使用Select来进行下拉框操作
sel = driver.find_element_by_xpath(".//*[@id='cooperation_type']")
# 从0开始
Select(sel).select_by_value('1')
# sela = driver.find_element_by_xpath(".//*[@id='bookss']/div[12]/div/select")
# Select(sela).select_by_value('1')
sela = driver.find_element_by_xpath(".//*[@id='bookss']/div[13]/div/select")
Select(sela).select_by_value('3')
print "集团编辑完成"
driver.find_element_by_xpath(".//*[@id='bookss']/div[14]/div[1]/button").click()
print "集团创建成功"
driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[9]/a[2]/button").click()
# sel = driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/select")
# Select(sel).select_by_value('2')
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div[1]/button").click()
driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[9]/a[3]/button").click()
print '集团已经分配给运营'

# 登录运营平台
def operatelogin(username,password):
    driver.get("http://woperate.test.4000669696.com")
    beforetitle = driver.title
    print u"登录之前的title -->  " + beforetitle
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys(username)
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    aftertitle = driver.title
    print u"现在的title -->  " + aftertitle
    if aftertitle == u"微语言  运营 后台 ":
        print u"title验证成功，运营平台登录成功"
    else:
        print u"title验证失败，运营平台登录失败"
    driver.refresh()

operatelogin("13426252525"+"123123")

driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/a/span").click()
time.sleep(5)
driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[11]/a[1]/button").click()
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(1)
print "进入集团管理员编辑页面"

admname = u"管gu理"
admpassd = "123123"

driver.find_element_by_xpath(".//*[@id='bookss']/div[16]/div/input").send_keys(admname)
driver.find_element_by_xpath(".//*[@id='bookss']/div[17]/div/input").send_keys(contactstel)
driver.find_element_by_xpath(".//*[@id='bookss']/div[18]/div/input").send_keys(admpassd)
driver.find_element_by_xpath(".//*[@id='bookss']/div[20]/div[1]/button").click()
# if判断返回的内容
print "集团管理员设置成功"
time.sleep(3)

# 登录新集团平台
def newgrouplogin(adname,adpassword):
    driver.get("http://" + groupadWebsite)
    beforetitle = driver.title
    print u"登录之前的title -->  " + beforetitle
    driver.find_element_by_xpath(".//*[@id='userName1']").send_keys(admname)
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(admpassd)
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/a").click()
    aftertitle = driver.title
    print u"现在的title -->  " + aftertitle
    if aftertitle == u"  分支 管理后台 ":
        print u"title验证成功，分支平台登录成功"
    else:
        print u"title验证失败，分支平台登录失败"

newgrouplogin()

# 获得当前的句柄
# sreach_window = driver.current_window_handle

