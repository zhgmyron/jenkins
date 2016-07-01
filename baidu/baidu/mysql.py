#coding:utf-8
import MySQLdb
class MySQLHelper(object):
    def __init__(self):
        pass
    @property
    def selectMySQL(self):
        try:
            conn= MySQLdb.connect(host ="localhost",user="root",passwd="root",db='test',charset="utf8")
            cur =conn.cursor()

        except Exception,e:
            print u'连接数据库失败'
        else:
            cur.execute('select * from writers;')
            data =cur.fetchall()
            for d in data:
                print d
        finally:
            cur.close()
            conn.close()
    @property
    def inserMySQL(self):

        try:
            conn= MySQLdb.connect(host ="localhost",user="root",passwd="root",db='test',charset="utf8")
            cur =conn.cursor()
            sql = 'insert into writers VALUES (%s,%s)'
            params =(20,'627')
            cur.execute(sql,params)
            conn.commit()

        except Exception,e:
            print u'连接数据库失败'
        else:
            print u'插入后表的数据'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()
    @property
    def updateMySQL(self):

        try:
            conn= MySQLdb.connect(host ="localhost",user="root",passwd="root",db='test',charset="utf8")
            cur =conn.cursor()
            sql = 'update writers set Name= %s where id=%s'
            params =('637',16)
            cur.execute(sql,params)
            conn.commit()

        except Exception,e:
            print u'连接数据库失败'
        else:
            print u'修改后表的数据'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()
    @property
    def deleteMySQL(self):

        try:
            conn= MySQLdb.connect(host ="localhost",user="root",passwd="root",db='test',charset="utf8")
            cur =conn.cursor()
            sql = 'delete from writers where id=%s'
            params =(17)
            cur.execute(sql,params)
            conn.commit()

        except Exception,e:
            print u'连接数据库失败'
        else:
            print u's删除表后的数据：'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()
MySQLHelper().inserMySQL