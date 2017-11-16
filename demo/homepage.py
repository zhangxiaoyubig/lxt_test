# coding=utf-8

#销售登录模块
def salelogin(driver):
    #from selenium import webdriver
    #driver = webdriver.Chrome()
    driver.get("http://wsale.test.4000669696.com/")
    driver.maximize_window()
    beforetitle = driver.title
    print u"登录之前的title -->  " + beforetitle
    driver.find_element_by_xpath(".//*[@id='form1']/div[1]/input").send_keys("15011420126")
    driver.find_element_by_xpath(".//*[@id='form1']/div[2]/input").send_keys("123123")
    driver.find_element_by_xpath(".//*[@id='form1']/div[3]/button").click()
    aftertitle = driver.title
    print u"现在的title -->  " + aftertitle
    if aftertitle  ==  u"微语言 销售 后台" :
        print u"title验证成功，销售平台登录成功"
    else:
        print u"title验证失败，销售平台登录失败"