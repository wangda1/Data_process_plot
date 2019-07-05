# python

##  参考文献
- 廖雪峰的官方网站:https://www.liaoxuefeng.com/wiki/897692888725344/923029651584288
- matplotlib绘制各种图：https://mp.weixin.qq.com/s/iQ5T_0LrAl8s0gnSDaw1Fg
- matplotlib绘图各种demo:https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html
- 莫烦python:https://morvanzhou.github.io/
- Matolotlib中文文档：https://www.matplotlib.org.cn/gallery/statistics/customized_violin.html
- seaborn: http://seaborn.pydata.org/index.html

## input/output

### input
`name = input()`

### output 
```
print('hello, world')
print(200)
print(100+200)
print('The quick brown dox','jumps over') #逗号部分输出以空格隔开
```

## 数据类型

- python中的数据类型属于普通的数据类型，动态解释型语言，不需要进行变量的声明即可使用
- 字符串可以使用''单引号或者""双引号表示
- 布尔值： True, False
- 空值：　None。None 不能理解为0，０是有意义的，None是一个特殊的空值。
- not　运算符是单目运算符，not True -> False
- Python的整数大小没有限制，浮点数大小也没有限制，超出一定的范围就直接表示为inf（无限大）
- python中变量定义不能采用数字开头

> list和array的区别： list中存放的是指针，可以包含不同的数据类型；array中包含相同的数据类型。

### 数据类型转换
```
int()       #   
float()     #
str()       #
bool()      #
```

### 数据类型检查
```
isinstance()        #   对参数类型进行检查
if not isinstance(x,(int,float))
    raise TypeError('bad operand type')
```

## 数据结构

### list
> list是一种有序的集合，可以随时添加和删除其中的元素。
```
l = []
len()       #   返回list元素的个数
append()    #   添加元素到末尾
pop()       #   删除末尾的元素  pop(i)
insert(k,v) #   在指定位置插入元素
```

### tuple
> tuple有序列表，tuple与list类似，但是tuple一旦初始化就不能更改
> tuple在定义的时候，其中的元素就必须被确定下来，因此不包含append(),insert()方法

```
t = (1,2)
t = ()
t = (1)     #　定义只包含一个元素的元组
```
### 切片 slice
可以取 list/tuple的一部分，类似于matlab中的操作
```
[-1]    #   取最后一个元素
[-2:-1] #   取倒数第二个元素
[:10]   #   取0-9个元素
[::2]   #   每隔两个取一个元素
[:,1:2] #   选取固定列
```
### 产生固定间隔的数组
1) 使用`range`方法
```
for i in range(1,20,2):
    l.append(i)
```
2) 使用`np.arange`
```
np.arange(-20,20,2)
```

## 函数
```
def my_abd(x):
    if x >= 0:
        retunrn x
    else:
        return -x
```
- pass的用法，空语句，起到占位符的作用
```
if age >= 18:
    pass
```
- 函数体内没有`return`时，自动`return None`

- 函数可以同时返回多个值，但返回的其实是一个`tuple`


## 处理excel数据

### 数据读取模块 xlrd

```Python
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

```
### 数据写入模块 xlwt
```Python
##  写入表格数据
##  data 要写入的表格数据
##  name 表的名称
workbook = xlwt.Workbook(encoding = 'utf-8')

def write_xls(workbook,data,name):
    worksheet = workbook.add_sheet(name)
    for c in range(len(data)):
        for r in range(len(data[c])):
            #print('the data is: ',data[c][r])
            worksheet.write(r,c,data[c][r])
 
workbook.save(save_file)
```

### pandas


## matplotlib模块的使用
```
import matplotlib.pyplot as plt
plt.figure(1)   #   创建图表1
plt.figure(2)   #   创建图表2
plt.show()      #   显示所有图表
plt.subplots(figsize=(m,n)) #   绘制子图，大小为m*n
```
1) subplot()    #   创建子图
plt.subplot(223)    #   创建2*2的图表矩阵，绘制的子图为矩阵中３序号

2)  plot()      #   画函数图像
```
plot(xdata,ydata,label="sin(x)")    #   label表示图例
plot(xdata,ydata'ro')               #   ro表示红色圆点
```

3)  sca()       #   选择子图
```
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

plt.sca(ax1)
plt.plot(x,np.exp(x))

plt.sca(ax2)
plt.plot(x,np.sin(x))       #   一张表中的第一条线
plt.plot(x,np.sin(x/2))     #   一张表中的第二条线
plt.plot(x,np.sin(x/3))     #   一张表中的第三条线

plt.show()
```

### 不同图类型

plot()函数默认绘制曲线图

- 直方图
```
hist()      #   频率分布直方图
```
- 散点图
```
scatter(x,y,c='r',marker='o')   #   前者为颜色，后者为形状
plot(x_data,y_data,'ro')        #   使用 plot　的方法绘制散点图
```
- 饼图
```
pie()   
```

- 柱状图
柱状图可以分为：　简单柱状图，群族柱状图，栈形柱状图
栈形柱状图的画法：https://stackoverflow.com/questions/23189815/matplotlib-stacked-bar-chart-assertionerror-incompatible-sizes-argument-botto
```
bar(x_data,y_data,color=,align=,label=,bottom=)
```
bottom=，属性可以用于定义栈型柱状图，bottoｍ应该使用`np.array()`的方法，对底部数组进行连接

- 箱形图

参考：https://blog.csdn.net/hustqb/article/details/77717026
> 箱形图的关键在于几个四分位点，分别是箱子的上下边缘的1/4,3/4分位点，箱子中线的1/2分位点
```
boxplot(y_data)
```

- 小提琴图

参考：https://www.matplotlib.org.cn/gallery/statistics/customized_violin.html
> 小提琴图是将箱形图与密度图结合的一种图形，可从图中读取数据的分位点，及各个数据点的分布密度信息

具体图形见：https://www.matplotlib.org.cn/gallery/statistics/customized_violin.html

### 绘图
- 使用`seaborn`绘图

参考：https://www.jianshu.com/p/4b925654f506
```Python
sns.set(style="whitegrid", palette="pastel", color_codes=True)
# Load the example tips dataset
tips = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=tips)
sns.despine(left=True) # 不显示网格边框线
```
- 使用原生`matplotlib`绘图

步骤：
1. 使用`plt.violinplot`绘制原始图形
2. 使用`plt.vline`和`plt.scatter`绘制出需要的中轴线和中位点

### 代码习惯

1)　使用`plt`直接绘制


2) 使用`subplots()`的方法
```
fig,ax = plt.subplots()     #   返回图片对象和子图
ax.set_xticklabels(x_data)  #   可用于设置标签
ax.set_xticks()             #   可用于设置标签位置，这两者常配合使用
ax.set_xlabel()             #   设置xlabel
ax.set_ylabel()             #   设置ylabel
ax.set_title()              #   设置标题
ax.set_xlim()               #   设置x坐标轴数据范围
ax.set_ylim()               #   设置y坐标轴数据范围
ax.legend()                 #   设置图例：　ax.legend(loc='upper right')
```
**Question?**
- 坐标轴如何旋转（当字体过大时，需要旋转到竖直方向）

`plt.xticks(rotation=270)`

- 如何画出双坐标轴/双y轴的图？

`ax.twinx()`        #   表示共享x轴

### 图表的注释与标识
```
plt.legend()    #   显示图例
plt.title()     #   设置图标题
plt.xlabel()    #   设置x轴文字
plt.ylabel()    #   设置y轴文字
plt.xticks(rotation=,fontsize=,fig=()) #   设置坐标轴刻度的文字方向，字体大小，图形大小
```

### 设置图例、坐标轴、刻度大小
```
ax.set_xticks(fontsize=)        #   设置刻度字体大小
ax.set_xlabel(fontsize=)        #   设置坐标轴标签字体大小
ax.legend(fontsize=)            #   设置图例字体大小
``` 

### 加载txt文件并绘图

## Seaborn　
- [Seaborn](http://seaborn.pydata.org/index.html)
> Seaborn 是一种基于matplotlib的图形可视化python library。它提供了一种高度交互式界面
> Seaborn　其实是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，Seaborn作为matplotlib的补充，可以制作出更多特色的图。

## xlrd模块的使用
- 参考：https://blog.csdn.net/oxuzhenyi/article/details/72528561
关于单元格值获取方法参考：[xlrd](https://www.cnblogs.com/puresoul/p/7520198.html)
1) excel的读取：
从excel读取数据，首选从xlrd包导入open_workbook，打开excel文件，把每个sheet里的每一行每一列数据都读取出来
- open_workbook()


2) 获取sheet
- 获取所有sheet名字：　x1.sheet_names()
- 获取sheet数量：　    x1.nsheets
- 获取所有sheet对象：  x1.sheets()
- 通过sheet名查找：    x1.sheet_by_name("test")
- 通过索引查找：       x1.sheet_by_index(3)

3) 获取sheet的汇总数据
- 获取sheet名：       sheet1.name
- 获取总行数：        sheet1.nrows
- 获取总列数：       sheet1.ncols

4) 单元格批量获取     
- sheet.cell(row,column).value     #    获取单元格的值
- sheet.row_values(r)              #    返回r行的值--列表  sheet.row_values(r)[0]  获取单元格中的值

##  xlwt模块的使用
```
data = xlrd.open_workbook('D:/momo/grade4.xlsx')
table = data.sheets()[0]
nrows = table.nrows

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(r,0,count)
workbook.save('D:/momo/4.xls')
```



## numpy模块的使用(Numeric Python)

- np.array()

```
import numpy as np
np.pi       #   pi
np.sin()
np.exp()
np.linspace(start,end,step)
np.loadtxt(filename, delimiter=',')     #delimiter为分隔符
np.arange(start,end,step)               #   类似于 range
np.random.rand(n)                       #   随机构造n个0-1之间的数据
np.random.seed()                        #   伪随机种子
np.array()                              #   可以将 list　转换成 numpy　中的数组
np.dot                                  #   求矩阵乘积
np.inv                                  #   求矩阵的逆
np.transpose                            #   求转置
np.lstsq                                #   求最小二乘法
np.hstack([l,s])                        #   对具有相同行数的矩阵l,s进行列扩展
np.ones((m,n))                          #   生成m*n的１矩阵
np.zeros((m,n))                         #   生成m*n的０矩阵
np.reshape((m,n))                       #   对矩阵重组
np.percentile(np.array,n)               #   计算任意np数组的百分比分位点
np.clip(x,min,max)                      #   将数组x(np.array)限制在min与max之间，<min的为min,>max的为max
```

**注意：**
> np.array()两个相加属于向量加，list两个相加属于连接操作

## Pandas 模块的使用
- [ref](http://codingpy.com/article/a-quick-intro-to-pandas/)
```
import pandas as pd
```
pandas　读取 excel　数据，得到的数据类型主要有： series 与 dataframe
## scikit-learn　模块的使用

> 注：　在使用`sklearn`时，数据涉及到较多的向量与矩阵，因此常采用 `numpy`将数据进行规整，而不是原来的`list`。
### 安装
`sudo pip3 install -U scikit-learn`


### 线性回归
```
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```
三个主要的函数：
- train_test_split： 用于生成训练集与测试集
- linreg = LinearRegression()
- model=linreg.fit(X_train, y_train)


### k-means聚类
[参考](https://blog.csdn.net/huangfei711/article/details/78480078)



### 决策树(DecisionTreeClassifier)
> 决策树是一种基于分类和回归的非监督学习方法。目标是创建一个模型，通过从数据特性中推导出简单的决策规则来预测目标变量的值。

- 优势
1)  使用白盒模型。相比于人工神经网络的黑盒模型而言
2)  可以使用统计测试验证模型；
3)  能够处理多输出问题；
4)  能够处理数值和分类数据。相对于其他技术专门分析只有一种变量的数据集

- 常用的代码风格：
```
from sklearn import tree
X = [[0,0],[1,1]]
Y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
clf.predict([[2.,2.]])
```

### 神经网络
参考：　https://www.cnblogs.com/lc1217/p/6861499.html

## random模块
- random.random()       #   0到1之间的浮点数
- random.randint(a,b)   #   a,b之间的随意整数
- random.uniform(a,b)   #   a,b之间的随意浮点数
- choice(seq)           #   在一个非空序列中随机选出一个元素
- randrange(start,stop[,step=1])    #   
- random.shuffle()      #   将一个列表中的元素打乱
- random.sample(sequence,k) #   从有序序列中选k个作为一个片段返回
- random.seed()         #   设定随机数种子

## 注意：

１）　在使用 xlrd　读取数据后，应该先检查数据类型是否符合规定，是str，还是float/
