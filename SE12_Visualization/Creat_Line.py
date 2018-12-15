import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
import  random
from pylab import mpl

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#读取中文数据文件
data=pd.read_csv('test.csv',encoding='utf-8')
df=pd.read_csv('test.csv',encoding='utf-8')
a=df['date'].values
b=a.tolist()
year= [val[:5] for val in b]
month=[val[6:8] for val in b]

def line(a,b,c):
    '''生成第a、b、c三年的票房趋势折线图'''
    year1=str(a)
    year2=str(b)
    year3=str(c)
    #定义全局变量
    global df, df2,df3,df4
    #定义列表储存各月份的票房
    total_boxoffice1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #遍历获得1到9月份的票房数据
    for i in range(1,10):
        df2 = df[df['date'].str.contains(year1+'-0'+str(i))]
        df3 = df[df['date'].str.contains(year2+'-0'+str(i))]
        df4 = df[df['date'].str.contains(year3+'-0'+str(i))]
        print(df2)
        #累加获得当前年份的总票房
        total_boxoffice1[i-1] += df2['boxoffice'].sum()
        total_boxoffice2[i-1] += df3['boxoffice'].sum()
        total_boxoffice3[i-1] += df4['boxoffice'].sum()
    #遍历获得10到12月份的票房数据
    for i in range(10,13):
        df2 = df[df['date'].str.contains(year1+'-'+str(i))]
        df3 = df[df['date'].str.contains(year2+'-'+str(i))]
        df4 = df[df['date'].str.contains(year3+'-'+str(i))]
        #累加获得当前年份的总票房
        total_boxoffice1[i-1] += df2['boxoffice'].sum()
        total_boxoffice2[i-1] += df3['boxoffice'].sum()
        total_boxoffice3[i-1] += df4['boxoffice'].sum()
    i = range(1,13)
    print(total_boxoffice1)

    #以月份为横轴，票房为纵轴生成三年的票房趋势变化图
    plt.title("票房趋势折线图")
    plt.plot(i, total_boxoffice1, label=year1)
    plt.plot(i, total_boxoffice2, label=year2)
    plt.plot(i, total_boxoffice3, label=year3)
    plt.xticks(i, i[::1])
    plt.xlabel('月份')
    plt.ylabel('票房')
    #y轴+0.3为了显示更清晰，fontsize为设置文字大小
    for x, y in zip(i, total_boxoffice1):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    for x, y in zip(i, total_boxoffice2):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    for x, y in zip(i, total_boxoffice3):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    plt.legend()
    plt.savefig('Line.jpg')
    plt.show()
line(2016,2017,2018)