#coding:utf-8
#from appium import webdriver
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t
from selenium.webdriver.common.by import By

class Page(object):
    def __init__(self,driver):
        self.driver =driver

    def find_element(self,loc):
        try:
            #return self.driver.find_element(*loc)
            return self.driver.find_element_by_xpath(loc)
        except (NoSuchElementException,KeyError,ValueError,Exception),e:
            print'Error deatail:%s'%(e.args[0])
    @property
    def wait(self):
        t.sleep(3)
