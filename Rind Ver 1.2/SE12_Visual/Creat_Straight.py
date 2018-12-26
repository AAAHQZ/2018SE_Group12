from pyecharts import Bar
import sys
sys.path.append("..")
from SE12_Crawler import *

def GetData(year, season):
    # 获取数据
    if __name__ == '__main__':
        dataBase = wrappedSQL("../SE12_Data/movie.db")
    else:
        dataBase = wrappedSQL("./SE12_Data/movie.db")
    year_str = str(year)
    season_int = int(season)
    lst = []
    if (season_int == 1):  # 第一季度
        for i in range(0, 3):
            dateValue = "Date like '"+year_str+"-0"+str(i+1)+"%'"
            lst.extend(dataBase.SelData(Title='data', Value=dateValue))
    if (season_int == 2):  # 第二季度
        for i in range(3, 6):
            dateValue = "Date like '"+year_str+"-0"+str(i+1)+"%'"
            lst.extend(dataBase.SelData(Title='data', Value=dateValue))
    if (season_int == 3):  # 第三季度
        for i in range(6, 9):
            dateValue = "Date like '"+year_str+"-0"+str(i+1)+"%'"
            lst.extend(dataBase.SelData(Title='data', Value=dateValue))
    if (season_int == 4):  # 第四季度
        for i in range(9, 12):
            dateValue = "Date like '"+year_str+"-"+str(i+1)+"%'"
            lst.extend(dataBase.SelData(Title='data', Value=dateValue))
    dataBase.CloseDB()
    # 提取电影种类信息
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
    return [names, boxs]

def DrawStraight(year, season, lst):
    year_str = str(year)
    season_int = int(season)
    bar=Bar("票房份额",width=600,height=450)
    bar.add("%s,%d" % (year_str,season_int), lst[0], lst[1],mark_point=["max","min"])
    bar.render("../SE12_Cache/Straight.html")

# 饼状图
def Straight(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    try:
        lst = GetData(year, season)
        DrawStraight(year, season, lst)
        return 1
    except:
        return 0

if __name__ == "__main__":
    Straight(2017,1)