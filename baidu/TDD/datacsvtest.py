#coding:utf-8
import os,csv,xlrd
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
            ('selenium3.0','android'),
            ('selenium3.1','ios')
        ]
        write.writerows(data)
def readCsv():
    with open(data_dirs()+'/system.csv','rb') as f:
        rows=[]
        readers=csv.reader(f)
        next(readers,None)
        for row in readers:
            rows.append(row)
        return rows

def readExcel(rowValue,colValue):
    book=xlrd.open_workbook(data_dirs()+'/system.xlsx')
    sheet= book.sheet_by_index(0)
    return sheet.cell_value(rowValue,colValue)
if __name__=='__main__':
    writeCsv()
    print readCsv()