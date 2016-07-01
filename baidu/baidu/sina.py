#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t

def wait():
    t.sleep(2)
def typeUsername(driver,username):
    driver.find_emelement_by_name('username').clear()
    wait()
    driver.find_emelement_by_name('username').send_keys(username)
def typePassword(driver,password):
    driver.find_emelement_by_name('password').clear()
    wait()
    driver.find_emelement_by_name('password').send_keys(password)
def clickLogin(driver):
    wait()
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[3]/div[2]/div[6]/a").click()
def login(driver,username,password):
    typeUsername(driver,username)
    typePassword(driver,password)
    clickLogin(driver)
def getErrorText(driver):
    wait()
    return driver.find_element_by_xpath('//*[@id="layer_14666648242221"]/div/p/span[2]').text

