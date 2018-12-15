import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pylab import mpl

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#读取中文数据文件
data=pd.read_csv('Movies.csv',encoding='gbk')
df=pd.read_csv('Movies.csv',encoding='gbk')
#饼状图
def pie(year, season):
    '''绘制第year年第season季度的票房占比饼状图'''
    #定义全局变量
    global df,df2
    year1=str(year)
    season1=int(season)

    if(season1==1):     #第一季度
        df= data[data['date'].str.contains(year1+'-01')+data['date'].str.contains(year1+'-02') + data['date'].str.contains(year1+'-03')]
    if(season1==2):     #第二季度
        df= data[data['date'].str.contains(year1+'-04')+data['date'].str.contains(year1+'-05') + data['date'].str.contains(year1+'-06')]
    if(season1==3):     #第三季度
        df= data[data['date'].str.contains(year1+'-07')+data['date'].str.contains(year1+'-08') + data['date'].str.contains(year1+'-09')]
    if(season1==4):     #第四季度
        df= data[data['date'].str.contains(year1+'-10')+data['date'].str.contains(year1+'-11') + data['date'].str.contains(year1+'-12')]
    print(df.iloc[:, 0].size)
    
    #定义列表a来储存不同类型电影的票房
    a=[0,0,0,0,0]
    #定义列表genres来储存电影的类型名称
    genres = ['奇幻', '喜剧', '爱情', '动作', '恐怖']
    #统计不同类型电影的票房并存入列表a
    df2 = df[df['genre'].str.contains('奇幻')]
    a[0]=df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('喜剧')]
    a[1] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('爱情')]
    a[2] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('动作')]
    a[3] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('恐怖')]
    a[4] = df2['boxoffice'].sum()

    #定义列表boxs来储存票房非0的电影类型的相应票房
    boxs = []
    #定义列表names来储存票房非0的电影类型
    names = []
    #将票房非0的电影类型和相应票房存入列表
    for cnt in range(0,5):
        if a[cnt] != 0:
            boxs.append(a[cnt])
            names.append(genres[cnt])

    plt.xticks(np.arange(len(names)),names)
    plt.ylabel('电影票房')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)
    plt.title( year1 + '年第' + str(season) + '季度各类型电影票房直方图')
    rects = plt.bar(names, boxs, width = 0.3, bottom = None, align = 'center')
    #在直方图上显示数字
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % int(height))

    #生成的图片保存为stright.jpg
    plt.savefig('Stright.jpg')
    plt.show()
pie(2017,3)