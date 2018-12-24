import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Line
import  random
from pylab import mpl

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#读取中文数据文件
data=pd.read_csv('Movies.csv')
df=pd.read_csv('Movies.csv')
a=df['date'].values
b=a.tolist()
year= [val[:5] for val in b]
month=[val[6:8] for val in b]

def line(a,b,c):
    year1=str(a)
    year2=str(b)
    year3=str(c)
    global df, df2,df3,df4
    totalboxoffice1=[0,0,0,0,0,0,0,0,0,0,0,0]
    totalboxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totalboxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1,10):
        df2 = df[df['date'].str.contains(year1+'-0'+str(i))]
        df3 = df[df['date'].str.contains(year2+'-0'+str(i))]
        df4 = df[df['date'].str.contains(year3+'-0'+str(i))]
        #print(df2)
        totalboxoffice1[i-1] += df2['boxoffice'].sum()
        totalboxoffice2[i-1] += df3['boxoffice'].sum()
        totalboxoffice3[i-1] += df4['boxoffice'].sum()
    for i in range(10,13):
        df2 = df[df['date'].str.contains(year1+'-'+str(i))]
        df3 = df[df['date'].str.contains(year2+'-'+str(i))]
        df4 = df[df['date'].str.contains(year3+'-'+str(i))]
        totalboxoffice1[i-1] += df2['boxoffice'].sum()
        totalboxoffice2[i-1] += df3['boxoffice'].sum()
        totalboxoffice3[i-1] += df4['boxoffice'].sum()
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    line=Line("票房统计","折线图形式展开")
    line.add("%s" %year1,columns,totalboxoffice1,mark_point=["max","min"],is_smooth=True)
    line.add("%s" % year2, columns, totalboxoffice2, mark_point=["max", "min"],is_smooth=True)
    line.add("%s" % year3, columns, totalboxoffice3, mark_point=["max", "min"],is_smooth=True)
    line.render(path="Line.png")
    #i = range(1, 13)
    # print(totalboxoffice1)
    # plt.title("折线图")
    # plt.plot(i,totalboxoffice1,label=year1)
    # plt.plot(i, totalboxoffice2, label=year2)
    # plt.plot(i, totalboxoffice3, label=year3)
    # plt.xticks(i, i[::1])
    # plt.xlabel('month')
    # plt.ylabel('boxoffice')
    # for x, y in zip(i, totalboxoffice1):
    #     plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    # for x, y in zip(i, totalboxoffice2):
    #     plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    # for x, y in zip(i, totalboxoffice3):
    #     plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    # plt.legend()
    # plt.show()
line(2016,2017,2018)