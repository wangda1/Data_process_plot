#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 统计各个单元测试人数
import xlrd
from xlrd import open_workbook
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']

chapters2017_num=[]
chapterf2017_num=[]
chapters2018_num=[]
chapterf2018_num=[]
spring2017_data=[]
fall2017_data=[]
spring2018_data=[]
fall2018_data=[]

wb = open_workbook('/home/hadoop/桌面/py/res/mooc后台数据/图表展示.xlsx')

s = wb.sheet_by_index(0)
print('Sheet:',s.name)

def read_data(s,chapter_name):
    chapters2017_num=[]
    chapterf2017_num=[]
    chapters2018_num=[]
    chapterf2018_num=[] 
    for row in range(s.nrows):
        # print('the row is:',row)
        # print('row value is',s.row_values(row,1,2))
        # print('row type is',s.row_types(row,1,2))
        if s.row_values(row,1,2)[0]==chapter_name:
            chapters2017_num.append(s.cell(row,3).value)        # float
            chapterf2017_num.append(s.cell(row,4).value)
            chapters2018_num.append(s.cell(row,5).value)
            chapterf2018_num.append(s.cell(row,6).value)
    spring2017_data.append(sum(chapters2017_num))
    fall2017_data.append(sum(chapterf2017_num))
    spring2018_data.append(sum(chapters2018_num))
    fall2018_data.append(sum(chapterf2018_num))
    return

chapter = ['绪论测验题','运算放大器测验题','二极管及其基本电路测验题','场效应管及其放大电路测验题','双极结型三极管及其放大电路测验题','放大电路频率响应测验题','模拟集成电路测验题',
          '反馈放大电路测验题','功率放大电路测验题','信号处理与信号产生电路测验题','直流稳压电源测验题']
labels = ['绪论','运算放大器','二极管及其基本电路','场效应管及放大电路','双极结型三极管','放大电路频率响应','模拟集成电路',
          '反馈放大电路','功率放大电路','信号处理与产生电路','直流稳压电源']
l = [i for i in range(len(chapter))]

# 产生每章节测验的总人数
for i in chapter:
    read_data(s,i)

# 打印数据
print(spring2017_data,'\n')
print(fall2017_data,'\n')
print(spring2018_data,'\n')
print(fall2018_data,'\n')

# 绘制栈形柱状图
_,ax = plt.subplots()

ax.bar(l,np.array(spring2017_data),align='center')
ax.bar(l,np.array(fall2017_data),bottom=np.array(spring2017_data),align='center')
ax.bar(l,np.array(spring2018_data),bottom=np.array(fall2017_data)+np.array(spring2017_data),align='center')
ax.bar(l,np.array(fall2018_data),bottom=np.array(fall2017_data)+np.array(spring2017_data)+np.array(spring2018_data),align='center')

plt.xticks(rotation=45,fontsize=10)
ax.set_xticklabels(labels)
ax.set_xticks(l)
ax.set_xlabel(u'单元测验')
ax.set_ylabel(u'单元测试人数')
ax.set_title(u'参加单元测验人数分布')
plt.show()
