# coding=utf-8
from selenium import webdriver
# 导入Select用来获取下拉框
from selenium.webdriver.support.select import Select
import  homepage


driver = webdriver.Chrome()
driver.get("http://wsale.test.4000669696.com/")
# 最大化浏览器
driver.maximize_window()
beforetitle = driver.title
print u"登录之前的title -->  " + beforetitle
# 登录销售后台

'''
def salelogin(username,password):
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys(username)
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    aftertitle = driver.title
    print u"现在的title -->  " + aftertitle
    if aftertitle == u"微语言 销售 后台":
        print u"title验证成功，销售平台登录成功"
    else:
        print u"title验证失败，销售平台登录失败"
salelogin("15011420126","123123")

homepage.salelogin(driver)
'''

personname = u"销售1" #销售姓名
personpassword = "123123" #销售密码
persontel = "13683552243" #联系方式

driver.find_element_by_xpath("html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a").click()
driver.find_element_by_xpath("html/body/div[1]/div[1]/section[1]/a/button").click()

driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[1]/div/input").send_keys(personname)
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[2]/div/input").send_keys(personpassword)
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[3]/div/input").clear()
driver.find_element_by_xpath(".//*[@id='bookss']/div/div[3]/div/input").send_keys(persontel)

position = driver.find_element_by_xpath(".//*[@id='bookss']/div/div[4]/div/select") #职位
Select(position).select_by_value('2')
Gender = driver.find_element_by_xpath(".//*[@id='bookss']/div/div[4]/div/select") #性别
Select(Gender).select_by_value('2')

driver.find_element_by_xpath(".//*[@id='bookss']/div/div[6]/div[1]/button").click()
#获取元素内容
na = driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[1]").text
if na == personname:
    print "销售账号添加成功"
else:
    print "账号添加失败，请查看"

#验证是否为开启状态，如果不是就点击开启
go = driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[6]/a[2]/button").text
if go == "开启":
    print "现在为开启状态"
else:
    driver.find_element_by_xpath(".//*[@id='example1']/tbody/tr[1]/td[6]/a[2]/button").click()
    print "开启成功"