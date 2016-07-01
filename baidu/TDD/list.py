#coding:utf-8
def getList():
    list=[['','',u'请您填写手机/邮箱/用户名'],['admin','',u'请您填写密码'],['admin','admin',u'请输入验证码']]
    return list
list1=['selenium1','selenium2','webdriver','appium','robotium']

print list1

list1.append('Android')
print list1

list1.remove('appium')
print list1
#分片访问  list1[m:n]，结果会包含m，不会包含n
print list1[0:4]

list2=['python','java','c#','c','c++']
list=[list1,list2]

print list

def func(*value1,**v):
    pass