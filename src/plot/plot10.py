#!/usr/bin/python3
#-*-coding:utf-8-*-

from xlrd import open_workbook
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']  #   显示中文不乱码
plt.rcParams['axes.unicode_minus'] = False  #   显示负数不乱码

##  绘制单元测验参加比例分布图, 重点：群族柱状图：关于x坐标的调整
##  绘制单元测验合格率分布图

##  读取表数据
def read_data(filename,sheet):
    wb = open_workbook(filename)
    s = wb.sheet_by_index(sheet)
    print(s.name)
    data = [[]for i in range(s.ncols)]
    for r in range(s.nrows):
        #    s.row_values(0)[0] 均为 float数据类型
        if r == 0:
            continue
        for c in range(s.ncols):
            data[c].append(s.row_values(r)[c])
    return data

file = '/home/hadoop/桌面/py/res/mooc后台数据/图表展示.xlsx'
chapter = ['绪论','运算放大器','二极管及其基本电路','场效应管及放大电路','双极结型三极管','放大电路频率响应','模拟集成电路',
          '反馈放大电路','功率放大电路','信号处理与产生电路','直流稳压电源']

##  qualified ratio     [0.95,0.92...]
qr = read_data(file,2)
##  qualified number
qn = read_data(file,1)
##  join ratio
jr = read_data(file,4)
print(jr)
_,ax = plt.subplots()

total_width = 0.8
ind_width = total_width / 4

alteration = np.arange(-(total_width/2),total_width/2,ind_width)

ax.bar(np.arange(len(jr[0]))+alteration[0],jr[1],label='2017春季',width=ind_width)
ax.bar(np.arange(len(jr[0]))+alteration[1],jr[2],label='2017秋季',width=ind_width)
ax.bar(np.arange(len(jr[0]))+alteration[2],jr[3],label='2018春季',width=ind_width)
ax.bar(np.arange(len(jr[0]))+alteration[3],jr[4],label='2018秋季',width=ind_width)

plt.xticks(rotation=45,fontsize=10)
ax.set_xticks(np.arange(len(jr[0])))
ax.set_xticklabels(chapter)
ax.set_ylim(0.1,0.7)
ax.set_xlabel('单元测验序号')
ax.set_ylabel('参加测验的比例')
ax.set_title('单元测验参加比例')
ax.legend(loc='upper right')

plt.show()
