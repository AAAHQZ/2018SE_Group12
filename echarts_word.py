#from wordcloud import WordCloud
import collections
from os import path
from pyecharts import  WordCloud
import matplotlib.pyplot as plt
import  pandas as pd
# 绘制词云
df=pd.read_csv('Movies.csv')
def pick_data(year,num):
    a=str(year)
    global df,df2                                          #选指定年份的数据
    df2=df[df['date'].str.contains(a)]
    df2=df2.sort_values(['boxoffice'],ascending=False)                      #找对应的票房
    data=df2.iloc[0:num]['name'].values  
    print(data)                             #找票房的前三位或者前几位
    return data


def draw_wordcloud(data,num):
    s1 = []
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
        #s1.append(s) 
        for j in range(i*2,50):                              #第一名的词循环写40次，第二名写30次，以此类推，利于词频统计
            s1.append(s)
    word_counts=collections.Counter(s1)        #统计词频
    #word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词

    keylist=[k[0] for k in word_counts.items()]                #找对应的电影名
    valuelist=[k[1] for k in word_counts.items()]              #电影名对应的词频

    wordcloud = WordCloud(width=680, height=500)
    wordcloud.add('wordcloud', keylist, valuelist, word_size_range=[int(0.9*13*(20/num)**0.5), int(0.9*39*(20/num)**0.5)],rotate_step=45)
    wordcloud.render("Wordcloud.html")
    plt.close()

if __name__ == '__main__':
    data = pick_data(2018, 10)
    print(data, 10)
    draw_wordcloud(data)
