#!/usr/bin/python3
#-*- coding: utf-8 -*-
import xlrd
from xlrd import open_workbook

x_data=[]
y_data=[]

wb = open_workbook('/home/hadoop/桌面/py/res/mooc后台数据/图表展示.xlsx')

for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        print('the row is:',row)
        values=[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)