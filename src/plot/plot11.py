#!/usr/bin/python3
#-*-coding:utf-8-*-

from xlrd import open_workbook
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']  #   显示中文不乱码
plt.rcParams['axes.unicode_minus'] = False  #   显示负数不乱码

##  绘制累计参加/退选人数分布图, 重点：群族柱状图：关于x坐标的调整

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

##  退选率表格
qr = read_data(file,13)
print(qr)
_,ax = plt.subplots()

total_width = 0.8
ind_width = total_width / 2

alteration = np.arange(-(total_width/2),total_width/2,ind_width)

ax.bar(np.arange(len(qr[0]))+alteration[0],qr[1],label='累积参加人数',color='r',width=ind_width)

ax2 = ax.twinx()
ax2.bar(np.arange(len(qr[0]))+alteration[1],qr[2],label='累积退选人数',color='g',width=ind_width)

#   set x ticks

plt.xticks(rotation=270)
ax.set_xticks(np.arange(len(qr[0])))
ax.set_xticklabels(['2017年春季','2017年秋季','2018年春季','2018年秋季'])
# ax.set_ylim(0.1,0.7)
ax.set_xlabel('年份')

#   set y label
ax.set_ylabel('累积参加人数')
ax2.set_ylabel('累积退选人数')


ax.set_title('累积参加/退选人数')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
