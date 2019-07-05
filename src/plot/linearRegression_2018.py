#!/usr/bin/python3
#-*-coding:utf-8-*-

#   多元线性回归 sklearn
#   表格中数据的位置：0-成绩；1-观看视频次数；2-单元测验次数；3-文档；４-随堂测验
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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
        # if r == 0:
        #     continue
        for c in range(s.ncols):
            data[c].append(s.row_values(r)[c])
    return data

s2017 = read_data(file,0)
x = np.array(s2017[1:4]).transpose()
y = np.array(s2017[0:1]).transpose()
X_train,X_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=100)



linreg = LinearRegression()
model = linreg.fit(X_train,y_train)

# x2 = [[1,3,5]]
# y2 = model.predict(x2)
# print(y2)
print(model) 
print(linreg.intercept_)            #   模型截距
print(linreg.coef_)                 #   模型特征值权重

y_pred = linreg.predict(X_test)
print (y_pred)    

#做ROC曲线
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label='predict')
plt.plot(range(len(y_pred)),y_test,'r',label='test')
plt.legend(loc='upper right') #显示图中的标签
plt.xlabel(u'观看视频，单元测验，文档')
plt.ylabel(u'成绩')
plt.title(u'多元线性回归分析')
plt.show()
