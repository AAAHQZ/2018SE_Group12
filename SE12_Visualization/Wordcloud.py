from wordcloud import WordCloud
import jieba
from scipy.misc import imread
from os import path
import matplotlib.pyplot as plt
import  pandas as pd
# 绘制词云
df=pd.read_csv('test.csv',encoding = 'UTF-8')
def pick_data(year,num):
    a=str(year)
    global df,df2
    df2=df[df['date'].str.contains(a)]
    df2=df2.sort_values(['boxoffice'],ascending=False)
    data=df2.iloc[0:num]['name'].values
    return data

def draw_wordcloud(data):
    s1 = []
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
        s1.append(s) 
        # for j in range(i*2,10):
        #     s1.append(s)

    cut_text=" ".join(s1)
    # print(cut_text)
    d = path.dirname(__file__)
    #color_mask = imread("background.jpg")  # 读取背景图片
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path="./uming.ttc",
        # 设置背景色
        background_color='white',
        # 词云形状
        #mask=color_mask,
        # 允许最大词汇
        max_words=400,
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
    plt.show()
    plt.close()

if __name__ == '__main__':
    data = pick_data(2018, 6)
    print(data)
    draw_wordcloud(data)