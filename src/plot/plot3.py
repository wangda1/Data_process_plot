#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 绘制绪论测验题的图
import xlrd
from xlrd import open_workbook
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']

score_data=[]
spring2017_data=[]
fall2017_data=[]
spring2018_data=[]
fall2018_data=[]

wb = open_workbook('/home/hadoop/桌面/py/res/mooc后台数据/图表展示.xlsx')

s = wb.sheet_by_index(0)
print('Sheet:',s.name)
for row in range(s.nrows):
    print('the row is:',row)
    print('row value is',s.row_values(row,1,2))
    print('row type is',s.row_types(row,1,2))
    if s.row_values(row,1,2)[0]=='绪论测验题':
        score_data.append(s.cell(row,2).value)
        spring2017_data.append(s.cell(row,3).value)
        fall2017_data.append(s.cell(row,4).value)
        spring2018_data.append(s.cell(row,5).value)
        fall2018_data.append(s.cell(row,6).value)
#print(isinstance(score_data[0],(float)))
print(score_data)
print(spring2017_data)
plt.plot(score_data,spring2017_data,label='2017春')
plt.plot(score_data,fall2017_data,label='2017秋')
plt.plot(score_data,spring2018_data,label='2018春')
plt.plot(score_data,fall2018_data,label='2018秋')
x_ticks=np.arange(0,20,2)
plt.xticks(x_ticks)
plt.xlabel(u'分数/分')
plt.ylabel(u'人数')
plt.title(u'绪论测验题')
plt.legend()
plt.show()
