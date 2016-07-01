#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,time

class keyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

        self.driver.implicitly_wait(3)
    def test_001(self):
        send =self.driver.find_element_by_id('kw')
        send.send_keys('webdriver')
        send.send_keys(Keys.CONTROL,'a')
        time.sleep(3)

        send.send_keys(Keys.CONTROL,'x')
        time.sleep(3)
        send.send_keys('webdriver')
        time.sleep(3)

        send.send_keys(Keys.CLEAR,'r')
        time.sleep(5)
        send.send_keys(Keys.ENTER)
        send.send_keys(Keys.F5)


    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)