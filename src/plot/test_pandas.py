#!/usr/bin/python3
#-*-coding:utf-8-*-

##  使用 pandas 读取表格数据
import pandas as pd


file = '/home/hadoop/桌面/py/res/mooc后台数据/个人行为信息02.xlsx'

pd_data = pd.read_excel(file)

print(pd_data[:0])
print(isinstance(pd_data[0],(list)))
