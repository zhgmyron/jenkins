#coding:utf-8
from selenium import webdriver
import time as t
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os,csv

def data_dirs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIRS=(os.path.join(BASE_DIR,'Data-Driven'),)
    d='/'.join(DATA_DIRS)
    return d
def writeCsv():
    with file(data_dirs()+'/system.csv','wb') as f:
        write=csv.writer(f)
        data=[
            ('selenium1','selenium2'),
            ('selenium3.0','android')
        ]
        write.writerows(data)

