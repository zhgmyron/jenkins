#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,time

class keyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

        self.driver.implicitly_wait(5)
    def test_001(self):
        send =self.driver.find_element_by_id('kw')
        send.send_keys('webdriver')
        send.find_element_by_id('su').click()
        time.sleep(3)

        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(3)
        js1="var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js1)


    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)
