#coding:utf-8
import time
class A(object):
    def __init__(self):
        pass
    def getInfo(self):
        print u'类的详细信息'
class B(object):
    def __init__(self):
        pass
    def show(self):
        print(u'显示类的详细信息')
    def getInfo(self):
        print u'b类的详细信息'
class C(A,B):
    def __init__(self):
        pass

c= C()

c.getInfo()
c.show()
print time.strftime('%Y-%m-%d',time.localtime(time.time()))