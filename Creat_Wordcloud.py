import wordcloud as wd
import collections
from os import path
from pyecharts import  WordCloud
import matplotlib.pyplot as plt
import  pandas as pd
from SE12_Crawler import *


# 绘制词云
def pick_data(year,num):
    year1 = str(year)
    # 读入文件
    db = wrappedSQL("movie.db")
    # 选择用户需要的年份
    lst = []
    dateValue = "Date like '"+year1+"%'"
    lst.extend(db.SelData(Title='data', Value=dateValue))
    print(lst)
    dicted = {}
    for item in lst:
        dicted[item["Movie"]] = float(item["BoxOffice"])
    L = sorted(dicted.items(), key=lambda item:item[1], reverse=True)
    # print(L)
    data = []
    for i in range(num):
        print(L[i][0])
        data.append(L[i][0])
    db.CloseDB() 
    return data


def draw_wordcloud(data,num):
    s1 = []
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
        #s1.append(s) 
        for j in range(i*2,50):
            s1.append(s)
    word_counts=collections.Counter(s1)        #统计词频
    #word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词

    keylist=[k[0] for k in word_counts.items()]
    valuelist=[k[1] for k in word_counts.items()]

    wordcloud = WordCloud(width=720, height=530)
    wordcloud.add('wordcloud', keylist, valuelist, word_size_range=[13*(20/num)**0.5,26*(1+0.02*num)*(20/num)**0.5],rotate_step=36.4)
    wordcloud.render("Wordcloud.html")

    s1 = []
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
        s1.append(s)
    cut_text=" ".join(s1)
    #print(cut_text)
    d = path.dirname(__file__)
    #color_mask = imread("background.jpg")  # 读取背景图片
    cloud = wd.WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path="res/simsun.ttc",
        # 设置背景色
        background_color='white',
        # 词云形状
        #mask=color_mask,
        # 允许最大词汇
        max_words=100,
        # 最大号字体
        max_font_size=64,
        #最小号字体
        min_font_size=16,
        #字体大小和频率相关性
        #relative_scaling=1
    )
    word_cloud = cloud.generate(cut_text)  # 产生词云
    word_cloud.to_file("WordCloud.jpg")  # 保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    #plt.show()
    plt.close()

if __name__ == '__main__':
    data = pick_data(2018, 10)
    print(data, 10)
    draw_wordcloud(data,10)