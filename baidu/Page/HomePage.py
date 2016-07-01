#coding:utf-8

from selenium import webdriver

import time as t
from yuebaidu.Page.BasePage import Page
from selenium.webdriver.common.by import By

class HomePage(Page):
    niCheng_loc=(By.XPATH,".//*[@id='s_username_top']/span")

    def getNiCheng(self):
        self.wait()
        return self.find_element(*self.niCheng_loc).text