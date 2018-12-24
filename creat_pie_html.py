import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Pie
from pylab import mpl
import pdfkit
from SE12_Crawler import *

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



# 饼状图
def pie(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    # 定义全局变量
    year1 = str(year)
    season1 = int(season)

    if (season1 == 1):  # 第一季度
        df = data[data['date'].str.contains(year1 + '-01') + data['date'].str.contains(year1 + '-02') + data[
            'date'].str.contains(year1 + '-03')]
    if (season1 == 2):  # 第二季度
        df = data[data['date'].str.contains(year1 + '-04') + data['date'].str.contains(year1 + '-05') + data[
            'date'].str.contains(year1 + '-06')]
    if (season1 == 3):  # 第三季度
        df = data[data['date'].str.contains(year1 + '-07') + data['date'].str.contains(year1 + '-08') + data[
            'date'].str.contains(year1 + '-09')]
    if (season1 == 4):  # 第四季
        df = data[data['date'].str.contains(year1 + '-10') + data['date'].str.contains(year1 + '-11') + data[
            'date'].str.contains(year1 + '-12')]
    # print(df.iloc[:, 0].size)

    # 定义列表a来储存不同类型电影的票房
    a = [0, 0, 0, 0, 0]
    # 定义列表genres来储存电影的类型名称
    genres = ['动画', '喜剧', '爱情', '动作', '冒险']
    # 统计不同类型电影的票房并存入列表a
    df2 = df[df['genre'].str.contains('动画')]
    a[0] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('喜剧')]
    a[1] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('爱情')]
    a[2] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('动作')]
    a[3] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('冒险')]
    a[4] = df2['boxoffice'].sum()

    # 定义列表boxs来储存票房非0的电影类型的相应票房
    boxs = []
    # 定义列表names来储存票房非0的电影类型
    names = []
    # 将票房非0的电影类型和相应票房存入列表
    for cnt in range(0, 5):
        if a[cnt] != 0:
            boxs.append(a[cnt])
            names.append(genres[cnt])

    # 列表names和列表boxs绘制饼状图
    dict1 = {'name': names, 'box': boxs}
    a1=[]
    a2=[]
    for (k,v) in dict1.items():
        a1.append(k)
        a2.append(v)

    #df2 = pd.DataFrame(dict1)
    print(names)
    print(boxs)
    image=Pie("票房占比",width=600,height=450)
    image.add("",names,boxs,is_label_show=True)
    image.render("Pie.html")

    df2 = pd.DataFrame(dict1)
    plt.pie(df2['box'], labels=df2['name'], autopct='%2.0f%%', explode = [0.05]*len(boxs))
    plt.title( year1 + '年第' + str(season) + '季度各类型电影票房占比饼状图')
    plt.savefig('Pie.jpg')
    plt.close()

#pie(2018, 1)