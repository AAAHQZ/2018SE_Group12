# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import re
import sys
if __name__ == '__main__':
    from baseCrawler import *
else:
    from .baseCrawler import *

<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
# pip3 install fontTools
# from fontTools.ttLib import TTFont

from .baseCrawler import baseCrawler
from .wrappedSQL import wrappedSQL

=======
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py


class maoyanCrawler(baseCrawler):
    """
    猫眼爬虫
    """ 
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
    # 测试
=======
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
    isUnit = 1
    csvdatas = [['name', 'boxoffice', 'Unit', 'Director', 'genre', 'date', 'actor'],]
    urlList = []
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
        # ____________________________________________
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
        # 查询总票房
        self.urlList = re.findall(r'''<ul class=\\"canTouch\\" data-com=\\"hrefTo,href:'(.*?)'\\">\\n''',self.newdata)
        return

    def DataParser(self):
        """
        根据urlList获取电影数据
        """
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
        # 正式版需要修改title
=======
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
        args={'title':"data",
        'Movie':"", 
        'BoxOffice':"", 
        'Unit':"",
        'Director':"", 
        'Category':"", 
        'Actor':"",
        'Date':""}
        self.payload ={}
        for item in self.urlList:
            self.URL = self.baseURL+item
            # 测试
            if __name__ == "__main__":            
                print(self.URL)
            self.GetReq()
            args['Movie'] = re.findall(r"<title>(.*)</title>", self.newdata)
            args['Movie'] = str(args['Movie'][0])
            # 电影信息已存在，只需要更新boxoffice
            flag = 0
            for i in range(len(self.csvdatas)):
                if self.csvdatas[i][0] == args['Movie']:
                    flag = 1
                    break
            args['BoxOffice'] = re.findall(r'''<span class="detail-num">(.*?)</span>''', self.newdata)
            if args['BoxOffice'] == []: continue
            args['BoxOffice'] = args['BoxOffice'][0]
            # 是否进行单位换算
            if self.isUnit == 1:
                if args['Unit'] == "亿":
                    num = float(args['BoxOffice'])
                    num = num*10000
                    args['BoxOffice'] = str(num)
                    args['Unit'] = "万"
            if flag == 1: continue
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
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py

            # 是否进行单位换算
            if self.isUnit == 1:
                if args['Unit'] == "亿":
                    num = float(args['BoxOffice'])
                    num = num*10000
                    args['BoxOffice'] = str(num)
                    args['Unit'] = "万"
            # 测试
            

            temp = [args['Movie'], str(int(float(args['BoxOffice']))), args['Unit'], args['Director'], args['Category'], args['Date'], args['Actor']]
            self.csvdatas.append(temp)
            print(temp)
=======
            # 缓存数据
            temp = [args['Movie'], str(int(float(args['BoxOffice']))), args['Unit'], args['Director'], args['Category'], args['Date'], args['Actor']]
            self.csvdatas.append(temp)
            # 测试
            if __name__ == "__main__":            
                print(temp)
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
        return 

        def ToCsv(self, filename):
            """
            将csvdatas写入csv文件
            """
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
            # filename = "./test.csv"
=======
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
            with open(filename, 'w', newline='', encoding = 'UTF-8') as f:
                writer = csv.writer(f)
                for row in self.csvdatas:
                    writer.writerow(row)
            return

<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
    def ToSql(self): 
        def insert():
            temp = self.csvdatas.pop(1)
            # if __name__ == "__main__":
                # print(temp)
            tempvalue = "Movie = '"+ temp[0] +"'"
            print(tempvalue)
            sel = self.db.SelData(Title=self.table,Value=tempvalue)
=======
    def ToSql(self):
        def insert():
            # 出队1个数据
            temp = self.csvdatas.pop(1)
            SQLValue = "Movie = '"+ temp[0] +"'"
            # 测试
            if __name__ == "__main__":            
                print(SQLValue)
            sel = self.db.SelData(Title=self.table,Value=SQLValue)
            # 判断插入或更新
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
            if sel == []:
                self.db.InsData(Title=self.table,
                    Movie=str(temp[0]), 
                    BoxOffice=str(temp[1]),
                    Director=str(temp[3]), 
                    Category=str(temp[4]),
                    Actor=str(temp[6]),
                    Date=str(temp[5])[0:10])
            else:
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
                # print(sel)
                self.db.UpdateData(Title=self.table,
                    Data='BoxOffice',
                    NewData=temp[1],
                    Value=tempvalue)

            return

=======
                self.db.UpdateData(Title=self.table,
                    Data='BoxOffice',
                    NewData=temp[1],
                    Value=SQLValue)
            return
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
        while len(self.csvdatas)>1:
            insert()
        return
 
    def InitSql(self, dbname, table):
        self.table = table
        self.db = wrappedSQL(dbname)
        self.db.CreateTable(Title=self.table)
        return
    
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
=======
    # 测试
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
    def printSql(self):
        temp = self.db.execute("UPDATE data SET BoxOffice = 12.60 WHERE Movie = '无双'")
        for col in temp:
            print(col)

<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
def MovieCrawler(fromYear, fromMonth, toYear, toMonth):
    isUnit = 1
    url = "https://piaofang.maoyan.com"
    maoyan = maoyanCrawler(url)
    maoyan.InitSql('movie.db', 'data')
=======
def MovieCrawler(fromYear, fromMonth, toYear, toMonth, dbpath="../SE12_Data/movie.db"):
    isUnit = 1
    url = "https://piaofang.maoyan.com"
    maoyan = maoyanCrawler(url)
    maoyan.InitSql(dbpath, 'data')
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
    maoyan.GetReq()
    yearNum = abs(toYear - fromYear)
    # monthNum = (toMonth - fromMonth)
    month = toMonth
    for y in range(yearNum+1):
        year = toYear - y
        while month >= 1:
            maoyan.SearchDate(str(year),str(month),'')
            maoyan.UrlParser()
            maoyan.DataParser()
            if (year==fromYear and month==fromMonth):
<<<<<<< HEAD:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
                print("INS~~~")
                maoyan.ToSql()
                maoyan.printSql()
                return
            month = month - 1
        month = 12
    return 1

if __name__ == "__main__":
    MovieCrawler(2018, 2, 2018, 2)
    # url = "https://piaofang.maoyan.com"
    # maoyan = maoyanCrawler(url)
    # maoyan.InitSql('movie.db', 'data')
    # maoyan.printSql()


    # isUnit = 1
    # url = "https://piaofang.maoyan.com"
    # maoyan = maoyanCrawler(url)
    # maoyan.GetReq()
    # # maoyan.DisplayData()
    # # maoyan.GetTranslator()
    # for i in range(1):
    #     for j in range(3):
    #         year = 2018-i
    #         month = 12-j
    #         maoyan.SearchDate(str(year),str(month), '')
    #         maoyan.UrlParser()
    #         maoyan.DataParser()
    # maoyan.ToCsv("./test.csv")
=======
                # 测试
                if __name__ == "__main__":            
                    print("INS~~~")
                maoyan.ToSql()
                maoyan.printSql()
                return 1
            month = month - 1
        month = 12
    return 0

if __name__ == "__main__":
    MovieCrawler(2018, 12, 2018, 12)
 
>>>>>>> Huangquanzhe:Rind Ver 1.2/SE12_Crawler/maoyanCrawler.py
