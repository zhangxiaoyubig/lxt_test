# coding=utf-8
from selenium import webdriver
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("http://sale.test.4000669696.com/")
# 最大化浏览器
driver.maximize_window()


# 登录销售后台
def salelogin():
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("15011420126 ")
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("123123")
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    print "销售平台登录成功"
salelogin()

#driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/a/span").click()
driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a").click()
#搜索条件。1.集团名称2.销售负责人
tiaojian = driver.find_element_by_xpath("html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[1]/select")
Select(tiaojian).select_by_value('2')
#不确定要填什么
driver.find_element_by_xpath("html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[2]/input").send_keys(u"不知道填什么")
#来源情况。1.来源情况（全部）2.在线注册3.系统注册
laiyuan = driver.find_element_by_xpath("html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[3]/select")
Select(laiyuan).select_by_value('2')
#分配情况。1.未分配2.已分配
fenpei = driver.find_element_by_xpath("html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/form/div/div[4]/select")
Select(fenpei).select_by_value('2')
#合作关系。1.战略合作2.普通合作
hezuo = driver.find_element_by_xpath(".//*[@id='cooperation_type']")
Select(hezuo).select_by_value('2')

#driver.find_element_by_xpath(".//*[@id='search-btn']").click()

print"搜索完成"
