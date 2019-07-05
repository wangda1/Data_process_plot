#!/usr/bin/python3
#-*-coding:utf-8-*-

#   绘制 violin 图，使用 matplotlib.pyplot 的方法
#   使用 seanborn　可以更简单地绘制 violin 图形
#   群族 violin　图形
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xlwt
from xlrd import open_workbook
import random

plt.rcParams['font.sans-serif']=['SimHei']  #   显示中文不乱码
plt.rcParams['axes.unicode_minus'] = False  #   显示负数不乱码

chapter = ['绪论测验题','运算放大器测验题','二极管及其基本电路测验题','场效应管及其放大电路测验题','双极结型三极管及其放大电路测验题','放大电路频率响应测验题','模拟集成电路测验题',
          '反馈放大电路测验题','功率放大电路测验题','信号处理与信号产生电路测验题','直流稳压电源测验题']

#   寻找章节索引
def find_index(it,li):
    for i in range(len(li)):
        if it == li[i]:
            return i
    return None
#   获取基本单元测验成绩数据
#   0-类型；1-名称；2-分数；3-人数
#   返回数据为 11　个单元测验成绩 [ np.array ]
def read_data(filename,index):
    wb = open_workbook(filename)
    s = wb.sheet_by_index(index)
    print(s.name)
    data = [[] for i in range(11)]
    #data = np.array(np.array([]) for i in range(11))
    for r in range(s.nrows):
        #    s.row_values(0)[0] 均为 float数据类型
        index = find_index(s.row_values(r)[1],chapter)
        if index is not None:
            for i in range(int(s.row_values(r)[3])):
                data[index].append(int(s.row_values(r)[2]))
    for i in range(11):
        data[i] = np.array(data[i])
    return data
#   绘制 violin 图形　API
#   x_data,y_data,width为
def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('单元测验')

def violin(ax2,x_data,y_data,width,color):
    parts = ax2.violinplot(
            y_data, positions=x_data,showmeans=False, showmedians=False,
            showextrema=False,widths=width)

    for pc in parts['bodies']:
        pc.set_facecolor(color)
        pc.set_edgecolor('black')
        pc.set_alpha(1)

    quartile1 = []
    medians = []
    quartile3 = []
    for i in range(len(y_data)):
        q1, m, q3 = np.percentile(y_data[i], [25, 50, 75], axis=0)
        quartile1.append(q1)
        medians.append(m)
        quartile3.append(q3)
        print(q1,m,q3)
    whiskers = np.array([
        adjacent_values(sorted_array, q1, q3)
        for sorted_array, q1, q3 in zip(y_data, quartile1, quartile3)])
    whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]

    # inds = np.arange(1, len(medians) + 1)
    print(len(inds))
    print(len(medians))
    ax2.scatter(x_data, medians, marker='o', color='white', s=30, zorder=3)
    ax2.vlines(x_data, quartile1, quartile3, color='k', linestyle='-', lw=3)
    ax2.vlines(x_data, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)

#   统一成百分制
def normal_100(data):
    for i in range(len(data)):
        data[i] = np.around(data[i] / max(data[i]) * 100)
    return data

#   单个族的宽度计算
total_width = 0.8
ind_width = total_width / 4

alteration = np.arange(-(total_width/2),total_width/2,ind_width)

s2017_file = '/home/hadoop/桌面/py/res/mooc后台数据/2017春/20170119-20190322模拟电子技术基础成绩分布.xls'
f2017_file = '/home/hadoop/桌面/py/res/mooc后台数据/2017秋/20170706-20190322模拟电子技术基础成绩分布.xls'
s2018_file = '/home/hadoop/桌面/py/res/mooc后台数据/2018春/20180126-20190322模拟电子技术基础成绩分布.xls'
f2018_file = '/home/hadoop/桌面/py/res/mooc后台数据/2018秋/成绩分布.xls'

s2017 = read_data(s2017_file,0)
f2017 = read_data(f2017_file,0)
s2018 = read_data(s2018_file,0)
f2018 = read_data(f2018_file,0)

s2017_100 = normal_100(s2017)
f2017_100 = normal_100(f2017)
s2018_100 = normal_100(s2018)
f2018_100 = normal_100(f2018)

print(s2017_100)

fig,ax = plt.subplots()
inds = np.arange(1,12)
violin(ax,inds+alteration[0],s2017_100,ind_width,'#00ff00')
violin(ax,inds+alteration[1],f2017_100,ind_width,'#ff0000')
violin(ax,inds+alteration[2],s2018_100,ind_width,'#0000ff')
violin(ax,inds+alteration[3],f2018_100,ind_width,'#D43F3A')
# ax.violinplot(s2017_100)
plt.xticks(rotation=45)
set_axis_style(ax,['绪论','运算放大器','二极管及其基本电路','场效应管及放大电路','双极结型三极管','放大电路频率响应','模拟集成电路',
          '反馈放大电路','功率放大电路','信号处理与产生电路','直流稳压电源'])
ax.set_ylabel('成绩/分')
ax.set_title('不同单元测验成绩分布小提琴图')
plt.show()