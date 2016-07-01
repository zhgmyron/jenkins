#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from baidu import baidu
import time as t
from ddt import ddt,data,unpack
import list
@ddt
class baiduPage(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)
    #@data(('','',u'请您填写手机/邮箱/用户名'),('admin','',u'请您填写密码'),('admin','admin',u'请输入验证码'))
    @data(*list.getList())
    @unpack
    def testFailLogin(self,value1,value2,expected):
        baidu.clickLogin(self.driver)
        baidu.login(self.driver,value1,value2)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(baidu.getErrorText(self.driver),expected)

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
        unittest.main(verbosity=2)

