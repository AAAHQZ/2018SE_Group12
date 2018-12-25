from pyecharts import Line
import sys
sys.path.append("..")
from SE12_Crawler import *

def GetData(year1, year2, year3):
    year1_str=str(year1)
    year2_str=str(year2)
    year3_str=str(year3)
    total_boxoffice1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_boxoffice3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 读入文件
    dataBase = wrappedSQL("../SE12_Data/movie.db")
    # 从文件读取月份票房数据
    for i in range(9):
        dateValue = "Date like '"+year1_str+"-0"+str(i+1)+"%'"
        lst1 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+year2_str+"-0"+str(i+1)+"%'"
        lst2 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+year3_str+"-0"+str(i+1)+"%'"
        lst3 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])
            
    for i in range(9,12):
        dateValue = "Date like '"+year1_str+"-"+str(i+1)+"%'"
        lst1 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst1:
            total_boxoffice1[i] = total_boxoffice1[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+year2_str+"-"+str(i+1)+"%'"
        lst2 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst2:
            total_boxoffice2[i] = total_boxoffice2[i] + float(item['BoxOffice'])
        dateValue = "Date like '"+year3_str+"-"+str(i+1)+"%'"
        lst3 = dataBase.SelData(Title='data', Value=dateValue)
        for item in lst3:
            total_boxoffice3[i] = total_boxoffice3[i] + float(item['BoxOffice'])
    dataBase.CloseDB()
    return [total_boxoffice1, total_boxoffice2, total_boxoffice3]

def DrawLine(year1, year2, year3, lst):
    try:
        columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        line=Line("票房变化趋势",width=600,height=450)
        line.add("%s" % year1, columns, lst[0], mark_point=["max","min"])
        line.add("%s" % year2, columns, lst[1], mark_point=["max", "min"])
        line.add("%s" % year3, columns, lst[2], mark_point=["max", "min"])
        line.render(path = "../SE12_Cache/Line.html")
        return 1
    except:
        return 0

def line(year1, year2, year3):
    lst = GetData(year1, year2, year3)
    ret = DrawLine(year1, year2, year3, lst)
    return ret

if __name__ == "__main__":
    line(2016,2017,2018)