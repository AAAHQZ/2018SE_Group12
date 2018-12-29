import collections
from pyecharts import  WordCloud as WCD
import sys
sys.path.append("..")
from SE12_Crawler import *


# 绘制词云
def GetData(year,num):
    year1 = str(year)
    # 读入文件
    if __name__ == '__main__':
        dataBase = wrappedSQL("../SE12_Data/movie.db")
    else:
        dataBase = wrappedSQL("./SE12_Data/movie.db")
    # 选择用户需要的年份
    lst = []
    dateValue = "Date like '"+year1+"%'"
    lst.extend(dataBase.SelData(Title='data', Value=dateValue))
    #print(lst)
    dicted = {}
    for item in lst:
        dicted[item["Movie"]] = float(item["BoxOffice"])
    L = sorted(dicted.items(), key=lambda item:item[1], reverse=True)
    # print(L)
    data = []
    for i in range(num):
        data.append(L[i][0])
    dataBase.CloseDB() 
    return data


def DrawWordCloud(data,num):
    s1 = []
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
        # 按照排名和电影名字长度设置词云虚拟频率
        for j in range(i*2,60-len(data[i])):
            s1.append(s)
    word_counts=collections.Counter(s1)        #统计词频
    #word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词

    keylist=[k[0] for k in word_counts.items()]
    valuelist=[k[1] for k in word_counts.items()]
    wordcloud = WCD(width=725, height=530)
        
    wordcloud.add('wordcloud', keylist, valuelist, word_size_range=[13*(20/num)**0.5,26*(1+0.02*num)*(20/num)**0.5],rotate_step=36.4)
    wordcloud.render(path="./SE12_Cache/WordCloud.html")

def WordCloud(year, num):
    # try:
        data = GetData(year, num)
        DrawWordCloud(data, num)
        return 1
    # except:
        return 0

if __name__ == '__main__':
    WordCloud(2017, 10)