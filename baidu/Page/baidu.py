#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t
from Page.BasePage import Page
from selenium.webdriver.common.by import By

class Baidu(Page):
    click_loc=(By.XPATH,".//*[@id='u1']/a[7]")
    userName_loc=(By.ID,'TANGRAM__PSP_8__userName')
    password_loc=(By.ID,'TANGRAM__PSP_8__password')
    clickButton_loc=(By.ID,'TANGRAM__PSP_8__submit')
    error_loc=(By.XPATH,".//*[@id='TANGRAM__PSP_8__error']")

    def clickLogin(self):
        self.wait
        self.find_element(*self.click_loc).click()

    def typeUsername(self,username):
        self.wait
        self.find_element(*self.userName_loc).send_keys(username)

    def typePassword(self,password):
        self.wait
        self.find_element(*self.password_loc).send_keys(password)

    def clickButtonLogin(self):
        self.wait
        self.find_element(*self.clickButton_loc).click()

    def getErrorText(self):
        self.wait
        self.find_element(*self.error_loc).text

    def login(self,username,password):
        self.clickLogin()
        self.typeUsername(username)
        self.typePassword(password)
        self.clickButtonLogin()



print Baidu(Page).login('admin','admin')



