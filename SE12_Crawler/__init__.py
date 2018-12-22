# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import sqlite3

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d

class wrappedSQL:
    '''
    封装SQL操作的类，使用自带的sqlite3模块。
    '''
    def __init__(self, dbName):
        """
        构造函数，创建或打开数据库。
        需要传入dbName
        """
        self.name = dbName
        self.con =  sqlite3.connect(str(dbName))
        self.con.row_factory = dict_factory
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute('''CREATE TABLE text (Title text, BoxOffice text)''',)
            self.con.commit()
            print("create!")
        except sqlite3.OperationalError:
       	    print("open!")
            pass
    
    #创建表 
    #需要传入Title
    def CreateTable(self, **args):
        """
        创建表 
        需要传入Title
        """
        try:
            # Date改成date类型
            self.cursor.execute("CREATE TABLE "+args['Title']+" \
                (ID       INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,\
                Movie     TEXT                              NOT NULL,\
                BoxOffice TEXT                              NOT NULL,\
                Director  TEXT                              NOT NULL,\
                Category  TEXT                              NOT NULL,\
                Actor     TEXT                              NOT NULL,\
                Date      DATE                              NOT NULL)")
            self.con.commit()
            self.cursor.execute("INSERT INTO "+args['Title']+" (ID, Movie, BoxOffice, Director, Category, Actor, Date)\
                VALUES (0, 'Movie', 'BoxOffice', 'Director', 'Category', 'Actor', 'Date')")
            print("create!")
        except sqlite3.OperationalError:
            print("existed!")
        return

    def InsData(self, **args):
        """
        #插入数据
        #需要传入Title, ID, Movie, BoxOffice, Director, Category, Actor, Date
        """
        self.cursor.execute("INSERT INTO "+args['Title']+" (Movie, BoxOffice, Director, Category, Actor, Date)\
            VALUES (?, ?, ?, ?, ?, ?)",
            (args['Movie'], args['BoxOffice'], args['Director'], args['Category'], args['Actor'], args['Date'],))
        self.con.commit()
        return
        
    def DelData(self, **args):
        """
        #删除数据   
        #需要传入Title, Value(ID的值)
        """
        self.cursor.execute("DELETE FROM "+args['Title']+" WHERE ID = ? ",
            (args['Value']))
        self.con.commit()
        return

    
    def SelData(self, **args):
        """
        #查询数据
        #需要传入Title, Value
        """
        value = self.cursor.execute("SELECT * FROM "+args['Title']+
        " WHERE "+args['Value'])
        return value 
        
    def UpdateData(self, **args):
        """
        #更新数据
        #需要传入Title, Data, NewData, Key, Value
        """
        self.cursor.execute("UPDATE "+args['Title']+" SET "+args['Data']+" = ? \
            WHERE "+args['Key']+" = ?",
            (args['NewData'], args['Value']))
        self.con.commit()
        return 
        
    def CloseDB(self):
        """
        关闭数据库
        """
        self.con.commit()
        self.con.close()
        print("close!")
    
    def test(self):
        self.cursor.execute('PRAGMA table_info try')


if __name__ == "__main__":
    db = wrappedSQL('text.db')
    db.CreateTable(Title="try")
    try:
        db.InsData(Title="try", 
            # ID="1", 
            Movie="first", 
            BoxOffice="1000万",
            Director="AAA", 
            Category="教育片",
            Actor="A, B, C",
            Date="16-1-2")
        db.InsData(Title="try", 
            # ID="2", 
            Movie="second", 
            BoxOffice="500万", 
            Director="AAA", 
            Category="记录片", 
            Actor="A, B, C, D",
            Date="16-2-3")    
    except sqlite3.IntegrityError:
        print("existed!")
    item = db.SelData(Title="try", 
        Value="ID = 1")
    for col in item:
        print(col)
    db.CloseDB()
