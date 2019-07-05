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

##  数据归一化函数
def normalization(data):
        # print(np.max(data[i]))
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


#   读取 2017年春季学期数据
s2017 = read_data(file,0)
#   对数据进行归一化处理
normal_s2017 = [s2017[0],normalization(s2017[1]),normalization(s2017[2]),normalization(s2017[3]),normalization(s2017[4])]
#   对数据格式进行调整，以生成 train_test_split()需要的数据格式
x = np.array(normal_s2017[1:4]).transpose()
y = np.array(normal_s2017[0:1]).transpose()
#   训练集与测试集的生成，test_size = 0.2表示测试集在数据集中的占比，选取数据时用到的伪随机种子为100
X_train,X_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=100)

print(X_train)
print(y_train)

#   构建线性回归模型，并加入训练集进行模型训练
linreg = LinearRegression()
model = linreg.fit(X_train,y_train)

#   输出模型训练完毕后的参数
print(model) 
print(linreg.intercept_)            #   模型截距
print(linreg.coef_)                 #   模型特征值权重

#   对预测集代入模型进行预测，得到预测数据 y_pred
y_pred = linreg.predict(X_test)

#   做ROC曲线
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label='predict')
plt.plot(range(len(y_pred)),y_test,'r',label='test')
plt.legend(loc='upper right') 
plt.xlabel(u'数据点序号')
plt.ylabel(u'成绩')
plt.title(u'多元线性回归分析')
plt.show()

#========================================================================
#==                 模型检验部分
#========================================================================
#   对数据集进行转置
y_pred = y_pred.transpose()
y_test = y_test.transpose()
print(y_test)
print (y_pred)    
#   对 数据类型进行转化，由excel读取的数据为 str
y = []
for i in range(len(y_test[0])):
    y.append(float(y_test[0][i]))
print(y)
##  模型检验计算SSR与SST：　R-square = SSR / SST
#   计算　SSR
m_y = np.mean(y)
print(m_y)
SSR = np.dot((np.array(y_pred[0]) - m_y),(np.array(y_pred[0]) - m_y))

#   计算  SST
SST = np.dot((np.array(y) - m_y),(np.array(y) - m_y))

#   R-square
Rs = SSR / SST

print(Rs)
print(SSR)
print(SST)