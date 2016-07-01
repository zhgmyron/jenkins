#coding:utf-8
import os,csv,xlrd
import xml.dom.minidom
class DataHelper(object):
    def __init__(self):
        pass

    def data_dirs(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIRS=(os.path.join(BASE_DIR,'Data-Driven'),)
        d='/'.join(DATA_DIRS)
        return d
    def getList(self):
        list=[['','',u'请您填写手机/邮箱/用户名'],['admin','',u'请您填写密码'],['admin','admin',u'请输入验证码']]
        return list
    def readFile(self,index):
        f=file(self.data_dirs()+'/system.txt','r')
        d= f.readlines()
        f.close()
        return d[index]
    def readCsv(self,value1,value2):
        rows=[]
        data_file=open(self.data_dirs()+'/system.csv')
        reader=csv.reader(data_file)
        next(reader,None)
        for row in reader:
            rows.append(row)
        return ''.join(rows[value1][value2]).decode('gb2312')

    def readExcel(self,rowValue,colValue):
        book=xlrd.open_workbook(self.data_dirs()+'/system.xlsx')
        sheet=book.sheet_by_index(0)
        return sheet.cell_value(rowValue,colValue)
    def readExcels(self):
        rows=[]
        book=xlrd.open_workbook(self.data_dirs()+'/system.xlsx')
        sheet=book.sheet_by_index(0)
        for row in range(1,sheet.nrows):
            rows.append(list(sheet.row_values(row,0,sheet.ncols)))
        return rows

    def getXmlData(self,value):
        dom=xml.dom.minidom.parse(self.data_dirs()+'/system.xml')
        db=dom.documentElement
        name=db.getElementsByTagName(value)
        nameValue =name[0]
        return nameValue.firstChild.data

    def getXmlUser(self,parent,child):
        dom=xml.dom.minidom.parse(self.data_dirs()+'/system.xml')
        db=dom.documentElement
        itemlist=db.getElementsByTagName(parent)
        item=itemlist[0]
        return item.getAttribute(child)

print DataHelper().getXmlData('test')
print DataHelper().getXmlUser('failLogin1','expected')



