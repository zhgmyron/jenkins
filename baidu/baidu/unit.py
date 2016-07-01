#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,time

class keyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

        self.driver.implicitly_wait(3)
    def test_001(self):
        self.assertEqual(u'百度一下，你就知道',self.driver.title)
    def test_002(self):
        self.assertEqual('https://www.baidu.com/',self.driver.current_url)


    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)
