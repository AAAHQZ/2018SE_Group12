from wordcloud import WordCloud
import jieba
from imageio import imread
from os import path
import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from collections import Counter

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制劳模演员
def draw_top_actor(year, number):

    # 读入文件
    data = pd.read_csv('test.csv',encoding='utf-8')
    # 选择用户需要的年份
    data = data[data['date'].str.contains(str(year))]
    # 从文件中读取演员信息
    actor_name_list = [item for item in data['actor']]
    # 对演员进行分词
    actor_name_line = ""
    for actor in actor_name_list:
        actor = actor.replace(' ','')
        actor_name_line += ','+actor
    actor_name_line = actor_name_line.replace(',','',1)
    s_list = actor_name_line.split(',')
    # 新建字典，按照出演数量排序
    seted = set(s_list)
    
    dicted = {}
    for item in seted:
        dicted.update({item:s_list.count(item)})
    L = sorted(dicted.items(), key = lambda item:item[1], reverse = True)
    L = L[:int(number)] #降序，保留Top演员数量的数据
    print(L)
    # 将列表转化为字典
    new_dict = {}
    for l in L:
        new_dict[l[0]] = l[1]
    print(new_dict)
    # 演员名字保存在name中，出演数量保存在cnt中
    names = []
    cnt = []
    for key,value in new_dict.items():
        print(key,value)
        
        names.append(key)
        cnt.append(value)
        if(len(names) == int(number)):
            break
        
    
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
    plt.show()
    
    
    

if __name__ == '__main__':

    draw_top_actor(2017, 3)