#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t


def wait():
	t.sleep(2)

def clickLogin(driver):
	wait()
	driver.find_element_by_id('u1').find_element_by_class_name('lb').click()

def typeUsername(driver,username):
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(username)

def typePassword(driver,password):
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(password)

def clickButtonLogin(driver):
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__submit').click()

def getErrorText(driver):
	wait()
	return driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__error']").text

def login(driver,username,password):

	typeUsername(driver,username)
	typePassword(driver,password)


def getNiCheng(driver):
	wait()
	return driver.find_element_by_xpath(".//*[@id='s_username_top']/span").text

def exit(driver):
	wait()
	move=driver.find_element_by_xpath(".//*[@id='s_username_top']/span")
	ActionChains(driver).move_to_element(move).perform()
	wait()
	driver.find_element_by_xpath(".//*[@id='s_user_name_menu']/div/a[5]").click()



