#coding:utf-8
from selenium import webdriver
import time as t
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
t.sleep(2)
element=driver.find_element_by_id('u1').find_element_by_class_name('pf')
ActionChains(driver).move_to_element(element).perform()

t.sleep(2)
driver.find_element_by_class_name('setpref').click()
t.sleep(3)
select=Select(driver.find_element_by_class_name('search-setting').find_element_by_id('nr'))

select.select_by_visible_text(u'每页显示50条')

t.sleep(3)
driver.find_element_by_id('gxszButton').find_element_by_class_name('prefpanelgo').click()
t.sleep(3)
print driver.switch_to_alert().text
driver.switch_to_alert().accept()