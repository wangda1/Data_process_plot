#!/usr/bin/python3
#-*-coding:utf-8-*-

## 画出累计参加人数和选课人数折线图

import matplotlib.pyplot as plt
import numpy as np
import xlrd
from xlrd import open_workbook

plt.rcParams['font.sans-serif']=['SimHei']  #   显示中文不乱码
plt.rcParams['axes.unicode_minus'] = False  #   显示负数不乱码
## 这里定义读取表格数据的统一行为
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

def plot_doubley(data):
    x_data = [i for i in range(len(data[0]))]
    _,ax = plt.subplots()
    plt.xticks(rotation=225)
    ax.plot(x_data,data[2],'r',label=u'退选人数')
    ax.set_xlabel(u'时间')
    ax.set_xticks(x_data[::20])
    ax.set_xticklabels(data[0][::20])
    ax.set_ylabel(u'退选人数')
    ax2 = ax.twinx()
    ax2.plot(x_data,data[4],label=u'累积退选人数')
    ax2.set_ylabel(u'累积退选人数')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.set_title(u'2017春季退选人数走势')
    plt.show()

file = '/home/hadoop/桌面/py/res/mooc后台数据/图表展示.xlsx'
s2017 = read_data(file,5)
f2017 = read_data(file,6)
s2018 = read_data(file,7)
f2018 = read_data(file,8)

plot_doubley(s2017)