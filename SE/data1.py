import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from pylab import  mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#读取中文数据文件
data=pd.read_csv('a.csv',encoding='gbk')
df=pd.read_csv('a.csv',encoding='gbk')
#饼状图
def pie(year,season):
    global df,df2
    year1=int(year)
    season1=int(season)
    if(season1==1):
        df= data[(data['year'] == year1) & (data['month'] <=3)]
    if(season1==2):
        df= data[(data['year'] == year1) & (data['month'] <= 6)&(df['month']>3)]
    if(season1==3):
        df= data[(data['year'] == year1) & (data['month'] <= 9)&(df['month']>7)]
    if(season1==4):
        df= data[(data['year'] == year1) & (data['month'] <= 12)&(df['month']>9)]
    print(df.iloc[:, 0].size)
    a=[0,0,0,0,0]
    df2=df[df['genre'].str.contains('奇幻')]
    a[0]=df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('冒险')]
    a[1] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('爱情')]
    a[2] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('动作')]
    a[3] = df2['boxoffice'].sum()
    df2 = df[df['genre'].str.contains('恐怖')]
    a[4] = df2['boxoffice'].sum()
    dict1 = {'name': ['a', 'b', 'c', 'd', 'e'], 'box': [a[0], a[1], a[2], a[3], a[4]]}
    df2=pd.DataFrame(dict1)
    print(df2)
    plt.pie(df2['box'], labels=df2['name'])
    plt.show()
pie(2018,3)





# pie(2018,3)
# print(df['genre'].str.split('/',expand=True)

# if(df[0:1]['genre'].str.contains('动作')[0]):
#     print('yes')
#print(df[0:1]['genre'][0].split('/'))

