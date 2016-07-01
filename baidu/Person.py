#coding:utf-8
class Person:
    test =u'我是静态字段'
    def __init__(self,name):
        self.name = name
        print u'我是构造函数'
    def hello(self):
        print 'hell world!'

    @staticmethod
    def printf():
        print u'我是静态方法'

    @property
    def show(self):
        print u'我是特性方法'
    def __del__(self):
        print u'我是析构函数'


print Person.test
Person.printf()


print "+++++++++++++"
per =Person('app')
per.show

