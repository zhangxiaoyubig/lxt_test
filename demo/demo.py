#coding=utf-8

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://sale.test.4000669696.com/")

def logg(aa,bb):
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys(aa)
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys(bb)
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    print "销售平台登录成功"

logg("111","222")