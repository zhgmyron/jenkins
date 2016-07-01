#coding:utf-8
from yuebaidu.model import Model

def main():
    username=raw_input(u'请输入用户名：\n')
    passwd= raw_input(u'请输入密码：\n')
    user =Model.User()
    result=user.checkValidate(username,passwd)

    if not result:
        print u'用户验证失败'
    else:
        print u'欢迎登录xx系统'
if __name__=='__main__':
    main()
