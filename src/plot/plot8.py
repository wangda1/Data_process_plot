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

file = '/home/hadoop/桌面/py/res/mooc后台数据/个人行为信息.xlsx'
save_file = '/home/hadoop/桌面/py/res/mooc后台数据/个人行为信息02.xlsx'
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
    ax.plot(x_data,y_data,'ro',label='观看视频次数')
    # ax.plot(data[2],data[0],'bo',label='单元测试次数')
    # ax.plot(data[3],data[0],'go',label='文档')
    # ax.plot(data[])
    ax.set_xlabel(u'观看视频次数')
    ax.set_ylabel(u'成绩')
    ax.set_title(u'成绩与观看视频次数的分布')
    plt.show()
##  对数据进行shuffle操作
##  data    数组
##  ratio   分段数
def shuffle_data(data,ratio):
    temp = [[] for i in range(ratio)]
    qu = int(len(data) / ratio)
    for i in range(ratio):
        if i == ratio -1 :
            temp[i] = data[i*qu:]
            random.shuffle(temp[i])
            break
        temp[i] = data[i*qu : (i+1)*qu]
        random.shuffle(temp[i])
    r = []
    for i in range(ratio):
        r += temp[i]
    return r
    
##  写入表格数据
##  data 要写入的表格数据
##  name 表的名称
def write_xls(workbook,data,name):
    worksheet = workbook.add_sheet(name)
    for c in range(len(data)):
        for r in range(len(data[c])):
            #print('the data is: ',data[c][r])
            worksheet.write(r,c,data[c][r])
 
    
workbook = xlwt.Workbook(encoding = 'utf-8')

s2017 = read_data(file,0)
ns2017 = [[] for i in range(5)]
ns2017[0] = s2017[0]
s_data = shuffle_data(s2017[1],5)
ns2017[1] = s_data
s_data = shuffle_data(s2017[2],2)
ns2017[2] = s_data
s_data = shuffle_data(s2017[3],5)
ns2017[3] = s_data
s_data = shuffle_data(s2017[4],2)
ns2017[4] = s_data

write_xls(workbook,ns2017,u'2017年春季')

f2017 = read_data(file,1)
nf2017 = [[] for i in range(5)]
nf2017[0] = f2017[0]
s_data = shuffle_data(f2017[1],5)
nf2017[1] = s_data
s_data = shuffle_data(f2017[2],2)
nf2017[2] = s_data
s_data = shuffle_data(f2017[3],5)
nf2017[3] = s_data
s_data = shuffle_data(f2017[4],2)
nf2017[4] = s_data

write_xls(workbook,nf2017,u'2017年秋季')

s2018 = read_data(file,2)
ns2018 = [[] for i in range(5)]
ns2018[0] = s2018[0]
s_data = shuffle_data(s2018[1],5)
ns2018[1] = s_data
s_data = shuffle_data(s2018[2],2)
ns2018[2] = s_data
s_data = shuffle_data(s2018[3],5)
ns2018[3] = s_data
s_data = shuffle_data(s2018[4],2)
ns2018[4] = s_data

write_xls(workbook,ns2018,u'2018年春季')

f2018 = read_data(file,3)
nf2018 = [[] for i in range(5)]
nf2018[0] = f2018[0]
s_data = shuffle_data(f2018[1],5)
nf2018[1] = s_data
s_data = shuffle_data(f2018[2],2)
nf2018[2] = s_data
s_data = shuffle_data(f2018[3],5)
nf2018[3] = s_data
s_data = shuffle_data(f2018[4],2)
nf2018[4] = s_data

write_xls(workbook,nf2018,u'2018年秋季')

# plot_scatter(s_data,s2017[0])
# f2017 = read_data(file,1)
# s2018 = read_data(file,2)
# f2018 = read_data(file,3)

# plot_scatter(ns2017[2],ns2017[0])


workbook.save(save_file)






