#coding:utf-8
import unittest
from yuebaidu.baidu import baidu
from yuebaidu.model import Model
from yuebaidu.baidu import basetestcase

class baiduPage(basetestcase.BaseTestCase,Model.DataHelper):
    def testFailLogin(self):
        baidu.clickLogin(self.driver)
        baidu.login(self.driver,self.readExcel(1,0),self.readExcel(1,1))
        baidu.clickButtonLogin(self.driver)
        self.assertEqual(self.readExcel(1,2),baidu.getErrorText(self.driver))

if __name__=='__main__':
        unittest.main(verbosity=2)
