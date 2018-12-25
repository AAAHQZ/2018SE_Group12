from pyecharts import Bar
from collections import Counter
import sys
sys.path.append("..")
from SE12_Crawler import *

def GetData(year, number):
    year_str = str(year)
    # 读入文件
    dataBase = wrappedSQL("../SE12_Data/movie.db")
    # 选择用户需要的年份
    lst = []
    SQLValue = "Date like '"+year_str+"%'"
    # 从文件中读取演员信息
    lst.extend(dataBase.SelData(Title='data', Value=SQLValue))
    dataBase.CloseDB()
    actorNames = []
    for item in lst:
        temp = item['Actor'].split(',')
        if temp == ['']: 
            continue
        actorNames.extend(item['Actor'].split(','))
    actorNames_set = set(actorNames)
    # 统计演员出演次数
    actorCnt = Counter(actorNames)
    dicted = {}
    for actor,cnt in actorCnt.items():
        dicted[actor] = cnt
    actorCnt = sorted(dicted.items(), key=lambda item:item[1], reverse=True)
    # 提取劳模演员数据
    names = []
    cnt = []
    for item in actorCnt:
        names.append(item[0])
        cnt.append(item[1])
        if len(names) == number:
            break
    return [names,cnt] 

def DrawActor(year, number, lst):
    try:
        bar = Bar("劳模演员",width=600,height=450)
        bar.add("%s,%d" % (year,number), lst[0], lst[1], mark_point=["max","min"])
        bar.render(path="../SE12_Cache/Top_actor.html")
        return 1
    except:
        return 0

# 绘制劳模演员
def draw_top_actor(year, number):
    lst = GetData(year, number)
    ret = DrawActor(year, number, lst)
    print(ret)
    return ret

if __name__ == '__main__':

    draw_top_actor(2018, 5)
