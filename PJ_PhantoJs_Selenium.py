from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)
driver.find_element_by_id('form_email').clear()
driver.find_element_by_id('form_email').send_keys('账号')
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('密码')
driver.find_element_by_class_name('bn-submit').click()
print(driver.page_source)