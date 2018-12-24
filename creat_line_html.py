import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Line
import  random
from pylab import mpl

from SE12_Crawler import *

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def line(a,b,c):
    db = wrappedSQL("./SE12_Crawler/movie.db")
    year1=str(a)
    year2=str(b)
    year3=str(c)
    total_boxoffice1=[0,0,0,0,0,0,0,0,0,0,0,0]
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
    line=Line("票房变化趋势",width=600,height=450)
    line.add("%s" %year1,columns,total_boxoffice1,mark_point=["max","min"])
    line.add("%s" % year2, columns, total_boxoffice2, mark_point=["max", "min"])
    line.add("%s" % year3, columns, total_boxoffice3, mark_point=["max", "min"])
    line.render("Line.html")
    
    i = range(1, 13)
    plt.title("票房趋势折线图")
    plt.plot(i,total_boxoffice1,label=year1)
    plt.plot(i, total_boxoffice2, label=year2)
    plt.plot(i, total_boxoffice3, label=year3)
    plt.xticks(i, i[::1])
    plt.xlabel('month')
    plt.ylabel('boxoffice')
    for x, y in zip(i, total_boxoffice1):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    for x, y in zip(i, total_boxoffice2):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    for x, y in zip(i, total_boxoffice3):
        plt.text(x, y + 0.3, str(y), ha='center', va='bottom', fontsize=10.5)
    plt.legend()
    plt.savefig('Line.jpg')
    plt.close()

if __name__ == "__main__":
    line(2016,2017,2018)