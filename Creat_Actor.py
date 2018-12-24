from os import path
import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pyecharts import Bar
from SE12_Crawler import *

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制劳模演员
def draw_top_actor(year, number):
    year1 = str(year)
    # 读入文件
    db = wrappedSQL("./SE12_Crawler/movie.db")
    # 选择用户需要的年份
    lst = []
    dateValue = "Date like '"+year1+"%'"
    lst.extend(db.SelData(Title='data', Value=dateValue))
    # 从文件中读取演员信息
    actor_names = []
    for item in lst:
        actor_names.extend(item['Actor'].split(','))
    actor_names = set(actor_names)
    print(actor_names)
    # 新建字典，按照出演数量排序
    
    dicted = {}
    for actor in actor_names:
        dicted[actor] = 0
    for item in lst:
        for actor in actor_names:
            if actor in item["Actor"]:
                dicted[actor] = dicted[actor]+1
    L = sorted(dicted.items(), key=lambda item:item[1], reverse=True)

    print(L)
    names = []
    cnt = []
    for item in L:
        print(item[0],item[1])
        names.append(item[0])
        cnt.append(item[1])
        if(len(names) == int(number)):
            break
    
    bar = Bar("劳模演员",width=600,height=450)
    bar.add("%s,%d" % (year,number),names,cnt,mark_point=["max","min"])
    bar.render(path="Top_actor.html")
    
    plt.xticks(np.arange(len(names)),names)
    plt.ylabel('出演次数')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)
    plt.title('劳模演员统计图')
    rects = plt.bar(names, cnt, width = 0.3, bottom = None, align = 'center')
    #显示出演数量
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % int(height))
    plt.savefig('Top_actor.jpg')
    plt.close()
    db.CloseDB()

if __name__ == '__main__':

    draw_top_actor(2018, 5)
