import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Bar
from SE12_Crawler import *

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取中文数据文件


# 饼状图
def Straight(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    # 定义全局变量
    year1 = str(year)
    season1 = int(season)

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

    sorted(genres_boxoffice.items(), key=lambda item:item[1])
    if __name__ == "__main__":
        print(genres_boxoffice)

    for name,box in genres_boxoffice.items():
        names.append(name)
        boxs.append(box)
    bar=Bar("票房份额",width=600,height=450)

    bar.add("%s,%d" % (year1,season1),names,boxs,mark_point=["max","min"])
    bar.render("Straight.html")
    #bar.render(path="straight.png")

    plt.xticks(np.arange(len(names)),names)
    plt.ylabel('电影票房')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)
    plt.title( year1 + '年第' + str(season) + '季度各类型电影票房直方图')
    rects = plt.bar(names, boxs, width = 0.3, bottom = None, align = 'center')
    #在直方图上显示数字
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % int(height))

    plt.savefig('Stright.jpg')
    plt.close()

if __name__ == "__main__":
    Straight(2017,1)