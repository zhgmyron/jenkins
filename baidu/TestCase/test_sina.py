#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
class sinaPage(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://weibo.com/login.php')
        self.driver.implicitly_wait(30)
    def test_001(self,username=''):
        u'''验证:微博title'''
        self.assertEqual(u'微博-随时随地发现新鲜事',self.driver.title)
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
        unittest.main()