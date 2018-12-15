#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'



# import base64
import re

# pip3 install fontTools
# from fontTools.ttLib import TTFont

from __init__ import wrappedSQL
from baseCrawler import baseCrawler

isUnit = 0

class maoyanCrawler(baseCrawler):
    """
    猫眼爬虫
    """ 
    # 测试
    csvdatas = [['name', 'boxoffice', 'Unit', 'Director', 'genre', 'date', 'actor'],]
    urlList = []
    # db = wrappedSQL('movie.db')
    baseHeader = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'}
    payload = {'ver':'normal'}


    def SearchDate(self,year,month,day):
        """
        根据传入的年月日获取页面
        """
        # ___________
        #  |-year   /boxoffice/3?date=YYYY&cnt=10
        #  |-month  /boxoffice/2?date=YYYYMM&cnt=10
        #  |-day    /dayoffice?date=YYYY-MM-DD&cnt=10
        self.date = year
        if month == '':
            self.URL = self.baseURL + '/boxoffice/3'
        elif day == '':
            self.date = self.date + month
            self.URL = self.baseURL + '/boxoffice/2'
        else:
            self.date = self.date + '-' + month + 'day'
            self.URL = self.baseURL + '/dayoffice'

        self.header={'Host':'piaofang.maoyan.com',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'Accept':'*/*',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':self.URL,
            'X-Requested-With':'XMLHttpRequest',
            'Uid':'905699f8e0308b3c9b0470873e1f9fe4df851d3c',
            'Connection':'keep-alive'}
        self.payload={'date':self.date,'cnt':'10'}

        # 测试
        if __name__ == "__main__":
            print(self.date)
            print(self.URL)
        
        self.GetReq()
        
        return            

    def UrlParser(self):
        """
        根据获取的页面获取urlList = {url:boxoffice,}
        """
        # 直接查询当日/月票房
        # self.urlList = dict(zip(re.findall(r'''<ul class=\\"canTouch\\" data-com=\\"hrefTo,href:'(.*?)'\\">\\n''',self.newdata),
        #     re.findall(r'''<li class=\\"c2 \\">\\n        <b>(.*?)</b><br/>\\n''',self.newdata)))
        # 查询总票房
        self.urlList = re.findall(r'''<ul class=\\"canTouch\\" data-com=\\"hrefTo,href:'(.*?)'\\">\\n''',self.newdata)
        return

    def DataParser(self):
        """
        根据urlList获取电影数据
        """
        # 正式版需要修改title
        args={'title':"try",
        'Movie':"", 
        'BoxOffice':"", 
        'Unit':"",
        'Director':"", 
        'Category':"", 
        'Actor':"",
        'Date':""}
        self.payload ={}
        # self.GetTranslator()
        # for (item,boxoffice) in self.urlList.items():
        for item in self.urlList:
            self.URL = self.baseURL+item
            # 测试
            if __name__ == "__main__":            
                print(self.URL)
            self.GetReq()
            # print(self.newdata)
            args['Movie'] = re.findall(r"<title>(.*)</title>", self.newdata)
            args['Movie'] = str(args['Movie'][0])
            # 电影信息已存在，只需要更新boxoffice
            flag = 0
            for i in range(len(self.csvdatas)):
                if self.csvdatas[i][0] == args['Movie']:
                    flag = 1
                    break
            if flag == 1: continue
            
            args['BoxOffice'] = re.findall(r'''<span class="detail-num">(.*?)</span>''', self.newdata)
            if args['BoxOffice'] == []: continue
            args['BoxOffice'] = args['BoxOffice'][0]
            args['Unit'] = re.findall(r'''<span class="detail-unit">(.*?)</span>''', self.newdata)
            args['Unit'] = args['Unit'][0]
            args['Director'] = re.findall(r'''"director":"(.*?)"''', self.newdata)
            args['Director'] = str(args['Director'][0])
            args['Category'] = re.findall(r'''"category":"(.*?)"''', self.newdata)
            args['Category'] = str(args['Category'][0])
            args['Date'] = re.findall(r'''<span class="score-info ellipsis-1">(.*?)</span>''',self.newdata)
            args['Date'] = str(args['Date'][0])
            self.URL = self.URL[:-8]+ '/celebritylist'
            self.GetReq()
            actor = re.findall(r"<p class=\"p-item-name ellipsis-1\">(.*)</p>",self.newdata)
            actor = set(actor[1:])
            args['Actor'] = ','.join(actor)

            # 是否进行单位换算
            if isUnit == 1:
                if args['Unit'] == u"亿":
                    num = float(args['BoxOffice'])
                    num = num*10000
                    args['BoxOffice'] = str(num)
                    args['Unit'] = u"万"
            # 测试
            if __name__ == "__main__":    
                print(args)
            

            temp = [args['Movie'], args['BoxOffice'], args['Unit'], args['Director'], args['Category'], args['Date'], args['Actor']]
            self.csvdatas.append(temp)
        return 

    # def GetTranslator(self):
    #     # 测试
    #     self.transfont = maoyanAntiCrawler(self.data)
    #     return



# class maoyanAntiCrawler:
#     """
#     反击“猫眼电影”网站的反爬虫策略 https://www.freebuf.com/news/140965.html
#     """
#     def __init__(self,resData):
#         self.resData = resData
#         self.GetFont()
#         # 测试
#         # self.ToXML()
#         self.GetList()
#         return
    
#     def GetFont(self):
#         font = re.findall(r"data:application/font-woff;charset=utf-8;base64,(.*?)\) format",self.resData)
#         # print(font)
#         fontdata=base64.b64decode(font[0])  
#         f=open('./font.woff','wb')  
#         f.write(fontdata)  
#         f.close()  
#         return

#     def ToXML(self):
#         font = TTFont('./font.woff')
#         font.saveXML('./font.xml')
#         return

#     def GetList(self):
#         self.font = TTFont('./font.woff')   # 打开文件
#         gly_list = self.font.getGlyphOrder()     # 获取 GlyphOrder 字段的值
#         # for gly in gly_list[2:]:    # 前两个值不是我们要的，切片去掉
#         #    print(gly)
#         return gly_list
        
#     def ModifyData(self, data):
#         # print(data)
#         # 获取 GlyphOrder 节点
#         gly_list = self.font.getGlyphOrder()
#         # 前两个不是需要的值，截掉
#         gly_list = gly_list[2:]
#         # 枚举, number是下标，正好对应真实的数字，gly是乱码
#         for number, gly in enumerate(gly_list):
#             # 把 gly 改成网页中的格式
#             gly = gly.replace('uni', '&#x').lower() + ';'
#             # 如果 gly 在字符串中，用对应数字替换
#             if gly in data:
#                 data = data.replace(gly, str(number))
#         # 返回替换后的字符串
#         # print(data)
#         return data

if __name__ == "__main__":
    isUnit = 1
    url = "https://piaofang.maoyan.com"
    maoyan = maoyanCrawler(url)
    maoyan.GetReq()
    # maoyan.DisplayData()
    # maoyan.GetTranslator()
    for i in range(4):
        for j in range(12):
            year = 2018-i
            month = 12-j
            maoyan.SearchDate(str(year),str(month), '')
            maoyan.UrlParser()
            maoyan.DataParser()
    maoyan.ToCsv("./test.csv")
