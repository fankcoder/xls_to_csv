#coding=utf-8
import xlrd
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readxls(name):
    filename = '%s.xlsx' %name
    xlsdata = xlrd.open_workbook(filename)
    table = xlsdata.sheets()[0]
    nrows = table.nrows
    for each in range(0,nrows):
        rows = table.row_values(each)
        items = []
        for index,item in enumerate(rows):
            item = item.encode('utf-8')
            items.append(item)
        create(items, name)

def create(data, name):
    filename = '%s.csv' %name
    with open(filename,'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(data)

if __name__ == '__main__':
    readxls('ExcelName') #xls的文件名,不需要加格式后缀
