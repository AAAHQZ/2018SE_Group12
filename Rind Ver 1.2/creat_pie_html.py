import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Pie
from pylab import mpl
from SE12_Crawler import *

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



# 饼状图
def pie(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    # 定义全局变量
    db = wrappedSQL("movie.db")
    year1 = str(year)
    season1 = int(season)
    lst = []
    if (season1 == 1):  # 第一季度
        for i in range(0, 3):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 2):  # 第二季度
        for i in range(3, 6):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 3):  # 第三季度
        for i in range(6, 9):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 4):  # 第四季度
        for i in range(9, 12):
            dateValue = "Date like '"+year1+"-"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    db.CloseDB()
    
    genres = []
    genres_boxoffice = {}
    for item in lst:
        genres.extend(item['Category'].split(','))
    genres = set(genres)


    for genre in genres:
        genres_boxoffice[genre] = 0

    for item in lst:
        for genre in genres:
            if genre in item['Category']:
                genres_boxoffice[genre] = genres_boxoffice[genre] + float(item['BoxOffice'])

    names = []
    boxs = []

    sorted(genres_boxoffice.items(), key=lambda item:item[1], reverse=True)
    if __name__ == "__main__":
        print(genres_boxoffice)

    for name,box in genres_boxoffice.items():
        names.append(name)
        boxs.append(box)
    image=Pie("",width=600,height=450)
    image.add("",names,boxs,is_label_show=True)
    image.render("Pie.html")


if __name__ == "__main__":
    pie(2018, 1)