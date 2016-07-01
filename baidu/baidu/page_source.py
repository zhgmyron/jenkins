#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get('http://www.baidu.com')
locator=WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID,'kw')))
locator.send_keys('appium')


element= driver.find_element_by_id('kw')
driver.save_screenshot('baidu.png')
driver.get_screenshot_as_file('f:/baidu.png')
print element.size
print element.tag_name
print element.value_of_css_property('#kw')

