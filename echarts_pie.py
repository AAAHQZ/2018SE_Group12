import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Pie
from pylab import mpl

# 解决中文显示问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 读取中文数据文件
# data = pd.read_csv('Movies.csv')
# df = pd.read_csv('Movies.csv')


# 饼状图
def pie(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    # 定义全局变量
    # global df, df2
    year1 = str(year)
    season1 = int(season)
    lst = []
    if (season1 == 1):  # 第一季度
        # df = data[data['date'].str.contains(year1 + '-01') + data['date'].str.contains(year1 + '-02') + data[
        #     'date'].str.contains(year1 + '-03')]               #找出date里带有该年 然后找月份里面的01 02 03 月
        for i in range(0, 3):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 2):  # 第二季度
        # df = data[data['date'].str.contains(year1 + '-04') + data['date'].str.contains(year1 + '-05') + data[
        #     'date'].str.contains(year1 + '-06')]
        for i in range(3, 6):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 3):  # 第三季度
        # df = data[data['date'].str.contains(year1 + '-07') + data['date'].str.contains(year1 + '-08') + data[
        #     'date'].str.contains(year1 + '-09')]
        for i in range(6, 9):
            dateValue = "Date like '"+year1+"-0"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    if (season1 == 4):  # 第四季度
        # df = data[data['date'].str.contains(year1 + '-10') + data['date'].str.contains(year1 + '-11') + data[
        #     'date'].str.contains(year1 + '-12')]
        for i in range(9, 12):
            dateValue = "Date like '"+year1+"-"+str(i+1)+"%'"
            lst.extend(db.SelData(Title='data', Value=dateValue))
    # print(df.iloc[:, 0].size)
    genres = []
    genres_boxoffice = {}
    for item in lst:
        genres.extend(item['Category'].split(','))
    genres = set(genre)

    for genre in genres:
        genres_boxoffice[genre] = 0

    for item in lst:
        for genre in genres:
            if genre in item['Category']:
                genres_boxoffice[genre] = genres_boxoffice[genre] + item['BoxOffice']

    a1 = []
    a2 = []

    for name,box in genres_boxoffice.items():
        a1.append(name)
        a2.append(box)
    # 定义列表a来储存不同类型电影的票房
    # a = [0, 0, 0, 0, 0]
    # 定义列表genres来储存电影的类型名称
    # genres = ['动画', '喜剧', '爱情', '动作', '冒险']           #电影类型  ，这个你看下数据库有多少类型自己加进去
     
    # 统计不同类型电影的票房并存入列表a
    # df2 = df[df['genre'].str.contains('动画')]              #在电影类里面找到包含该相关词的电影数据
    # a[0] = df2['boxoffice'].sum()
    # df2 = df[df['genre'].str.contains('喜剧')]
    # a[1] = df2['boxoffice'].sum()
    # df2 = df[df['genre'].str.contains('爱情')]
    # a[2] = df2['boxoffice'].sum()
    # df2 = df[df['genre'].str.contains('动作')]
    # a[3] = df2['boxoffice'].sum()
    # df2 = df[df['genre'].str.contains('冒险')]
    # a[4] = df2['boxoffice'].sum()

    # 定义列表boxs来储存票房非0的电影类型的相应票房
    # boxs = []
    # 定义列表names来储存票房非0的电影类型
    # names = []
    # 将票房非0的电影类型和相应票房存入列表
    # for cnt in range(0, 5):
    #     if a[cnt] != 0:
    #         boxs.append(a[cnt])
    #         names.append(genres[cnt])

    # 列表names和列表boxs绘制饼状图
    # dict1 = {'name': names, 'box': boxs}
    # print(dict1)
    # a1=[]
    # a2=[]
    # for k,v in dict1.items():
    #     print()
    #     a1.append(k)
    #     a2.append(v)

    #df2 = pd.DataFrame(dict1)
    # print(a1)
    # print(a2)
    image=Pie("test",width=500,height=300)
    image.add("",a1,a2,is_label_show=True)
    image.render("Pie.html")
    image.render(path="Pie.png")
    # print(df2)
    # # 其中autopct用于在饼状图内部显示票房占比数字，explode用于使饼状图各块突出显示
    # plt.pie(df2['box'], labels=df2['name'], autopct='%2.0f%%', explode=[0.05] * len(boxs))
    # plt.title(year1 + '年第' + str(season) + '季度各类型电影票房占比饼状图')
    # # 生成的图片保存为Pie.jpg
    # plt.savefig('Pie.jpg')
    # plt.close()
    # plt.show()


pie(2018, 1)