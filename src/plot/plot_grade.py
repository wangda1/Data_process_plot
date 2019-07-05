### 绘制成绩（全部）的散点图
#!/usr/bin/python3

from xlrd import open_workbook
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']

filename0 = '/home/hadoop/桌面/py/res/mooc后台数据/2017春/20170119-20190322模拟电子技术基础成绩(全部).xls'
filename1 = '/home/hadoop/桌面/py/res/mooc后台数据/2017秋/20170706-20190322模拟电子技术基础成绩(全部).xls'
filename2 = '/home/hadoop/桌面/py/res/mooc后台数据/2018春/20180126-20190322模拟电子技术基础成绩(全部).xls'
filename3 = '/home/hadoop/桌面/py/res/mooc后台数据/2018秋/20180726-20190322模拟电子技术基础成绩(全部).xls'

def read_data(filename):
    wb = open_workbook(filename)
    score_data=[]
    s = wb.sheet_by_index(0)
    print('the sheet is:',s.name)
    for r in range(s.nrows):
        if r == 0:
            continue
    ## 成绩
    #print(s.cell(r,10).value)
        score_data.append(float(s.cell(r,10).value))
    # print(score_data)
    # print(isinstance(score_data[2],(str,)))
    # print(max(score_data))
    return score_data
_,ax=plt.subplots()
spring2017 = read_data(filename0)
fall2017 = read_data(filename1)
spring2018 = read_data(filename2)
fall2018 = read_data(filename3)
ax.boxplot([spring2017,fall2017,spring2018,fall2018])
ax.set_xticklabels(['2017春','2017秋','2018春','2018秋'])
ax.set_xlabel('年份')
ax.set_ylabel('成绩分布')
ax.set_title('成绩分布箱形图')
print(max(fall2017))
plt.show()

