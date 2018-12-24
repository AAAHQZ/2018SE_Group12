import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Line
import  random
from pylab import mpl

from SE12_Crawler import *


#解决中文显示问题
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

#读取中文数据文件
# data=pd.read_csv('Movies.csv')
# df=pd.read_csv('Movies.csv')
# a=df['date'].values
# b=a.tolist()
# year= [val[:5] for val in b]
# month=[val[6:8] for val in b]

def line(a,b,c):
    db = wrappedSQL("movie.db")
    year1=str(a)
    year2=str(b)
    year3=str(c)
    # global df, df2,df3,df4
    # totalboxoffice1=[0,0,0,0,0,0,0,0,0,0,0,0]
    # totalboxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # totalboxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(1,10):
    #     df2 = df[df['date'].str.contains(year1+'-0'+str(i))]
    #     df3 = df[df['date'].str.contains(year2+'-0'+str(i))]
    #     df4 = df[df['date'].str.contains(year3+'-0'+str(i))]
    #     #print(df2)
    #     totalboxoffice1[i-1] += df2['boxoffice'].sum()
    #     totalboxoffice2[i-1] += df3['boxoffice'].sum()
    #     totalboxoffice3[i-1] += df4['boxoffice'].sum()
    # for i in range(10,13):
    #     df2 = df[df['date'].str.contains(year1+'-'+str(i))]
    #     df3 = df[df['date'].str.contains(year2+'-'+str(i))]
    #     df4 = df[df['date'].str.contains(year3+'-'+str(i))]
    #     totalboxoffice1[i-1] += df2['boxoffice'].sum()
    #     totalboxoffice2[i-1] += df3['boxoffice'].sum()
    #     totalboxoffice3[i-1] += df4['boxoffice'].sum()
    
    total_boxoffice1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(9):
        dateValue = "Date like '"+str(a)+"-0"+str(i+1)+"%'"
        lst1 = db.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(b)+"-0"+str(i+1)+"%'"
        lst2 = db.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(c)+"-0"+str(i+1)+"%'"
        lst3 = db.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])
            
    for i in range(9,12):
        dateValue = "Date like '"+str(a)+"-"+str(i+1)+"%'"
        lst1 = db.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(b)+"-"+str(i+1)+"%'"
        lst2 = db.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+str(c)+"-"+str(i+1)+"%'"
        lst3 = db.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])

    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    line=Line("票房统计","折线图形式展开")
    line.add("%s" % year1, columns, total_boxoffice1, mark_point=["max","min"],is_smooth=True)
    line.add("%s" % year2, columns, total_boxoffice2, mark_point=["max", "min"],is_smooth=True)
    line.add("%s" % year3, columns, total_boxoffice3, mark_point=["max", "min"],is_smooth=True)
    line.render(path="./Line.png")
    db.CloseDB()
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