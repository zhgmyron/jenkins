#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import baidu
import time as t


class baiduPage(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)
    def test_001(self,username=''):
        u'''验证:用户名为空,点击登录返回的错误信息'''
        baidu.clickLogin(self.driver)
        baidu.typeUsername(self.driver,username)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(u'请您填写手机/邮箱/用户名',baidu.getErrorText(self.driver))
    def test_002(self,password='admin'):
        u'''验证:只输入密码，点击登录返回的错误信息'''
        baidu.clickLogin(self.driver)
        baidu.typePassword(self.driver,password)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(u'请您填写手机/邮箱/用户名',baidu.getErrorText(self.driver))

    def test_003(self,username='zhgjames@sina.com',password='Zxcvb1234567'):
        u'''验证:用户登录成功'''
        baidu.clickLogin(self.driver)
        baidu.login(self.driver,username,password)
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(u'rolllrol',baidu.getNiCheng(self.driver))
    def tearDown(self):
        self.driver.quit()
    @staticmethod
    def suite():
        #suite=unittest.TestLoader().loadTestsFromTestCase(baiduPage)
        suite=unittest.TestSuite(unittest.makeSuite(baiduPage))
        return suite

if __name__=='__main__':
    # suite=unittest.TestSuite()
    # suite.addTest(baiduPage('test_001'))
    # suite.addTest(baiduPage('test_002'))
    # suite.addTest(baiduPage('test_003'))
    #suite=unittest.TestSuite(unittest.makeSuite(baiduPage))
    unittest.TextTestRunner(verbosity=2).run(baiduPage.suite())