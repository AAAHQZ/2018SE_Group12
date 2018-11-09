# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

from __init__ import wrappedSQL
from baseCrawler import baseCrawler

import re

class betaCrawler(baseCrawler):
    """
    """
    movietable = {'Rank':['Title', 'Box Office']}
    db = wrappedSQL('text');
    
    def dataParser(self):
        self.titleit = re.finditer(r'><b>(.*)</b></a></font></td>', self.data, re.I|re.M)
        self.boxoit = re.finditer(r'<font size="2"><b>(.*)</b></font></td>', self.data, re.I|re.M)
        
    def SQLop(self):
        for title, boxoffice in zip(self.titleit, self.boxoit):
            sql = self.handle(title.group(1),boxoffice.group(1))
            self.db.insData(sql)
            
    def displayData(self):
        item = self.db.selData('''select * from text''')
        all_item = item.fetchall()
        for output in all_item:
            print(output)
            
    def handle(self, str1,str2):
        sql = [[],[]]
        sql[0] = '''insert into text (Title, BoxOffice) values (?, ?)'''
        sql[1]=[str1,str2]
        return sql
     
            
         
if __name__ == "__main__":
    url = 'https://www.boxofficemojo.com/alltime/world/'
    bomj = betaCrawler(url)
    bomj.getReq()
    bomj.dataParser()
    bomj.displayData()

