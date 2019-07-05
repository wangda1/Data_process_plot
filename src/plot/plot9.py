#!/usr/bin/python3
#-*-coding:utf-8-*-

#   绘制成绩与各用户行为数据之间的散点图
#   表格中数据的位置：0-成绩；1-观看视频次数；2-单元测验次数；3-文档；４-随堂测验
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xlwt
from xlrd import open_workbook
import random

plt.rcParams['font.sans-serif']=['SimHei']  #   显示中文不乱码
plt.rcParams['axes.unicode_minus'] = False  #   显示负数不乱码


file = '/home/hadoop/桌面/py/res/mooc后台数据/个人行为信息02.xlsx'

##  读取表数据
def read_data(filename,sheet):
    wb = open_workbook(filename)
    s = wb.sheet_by_index(sheet)
    data = [[]for i in range(s.ncols)]
    for r in range(s.nrows):
        #    s.row_values(0)[0] 均为 float数据类型
        if r == 0:
            continue
        for c in range(s.ncols):
            data[c].append(s.row_values(r)[c])
    return data

##  绘制散点图
def plot_scatter(x_data,y_data):
    _,ax = plt.subplots()
    ax.plot(x_data,y_data,'co',label='次数')
    # ax.plot(data[2],data[0],'bo',label='单元测试次数')
    # ax.plot(data[3],data[0],'go',label='文档')
    # ax.plot(data[])
    ax.set_xlabel(u'单元测验次数')
    ax.set_ylabel(u'成绩')
    ax.set_title(u'成绩与单元测验次数的分布')
    plt.show()
    


s2017 = read_data(file,0)
# f2017 = read_data(file,1)
# s2018 = read_data(file,2)
# f2018 = read_data(file,3)

plot_scatter(s2017[3],s2017[0])







