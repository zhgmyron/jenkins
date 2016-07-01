#coding:utf-8
import unittest
from yuebaidu.Page.baidu import Baidu
from yuebaidu.Page.BasePage import Page
from yuebaidu.Page.HomePage import HomePage
from yuebaidu.Page.basetestcase import BaseTestCase
from yuebaidu.model import Model
from ddt import ddt,data,unpack

class baiduPage(BaseTestCase,Baidu,HomePage,Model.DataHelper):


    def testFailLogin(self):

        self.login(self.readExcel(1,0),self.readExcel(1,1))

        self.assertEqual(self.readExcel(1,2),self.getErrorText(self.driver))
if __name__=='__main__':
    unittest.main(verbosity=2)
