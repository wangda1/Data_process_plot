#定义生成观看次数函数，参数是成绩，返回值是观看次数
import random
def ViewValue(g):
    k = 0.426*(random.uniform(0.5,1.5))
    n = round(float(k)*float(g))
    return n

#定义读取和写入函数
import re
import xlrd
import xlwt
import numpy as np
data = xlrd.open_workbook('D:/momo/grade4.xlsx')
table = data.sheets()[0]
nrows = table.nrows

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

for r in range(nrows):
    count = ViewValue(table.cell(r,0).value)
    worksheet.write(r,0,count)
    #worksheet.write(r,1,count)
    #worksheet.write(r,2,count)
    #worksheet.write(r,3,count)
workbook.save('D:/momo/4.xls')
