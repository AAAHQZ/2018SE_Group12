#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import sqlite3

#封装SQL操作的类，使用自带的sqlite3模块。
class wrappedSQL:
    '''
    
    '''
    #构造函数，创建或打开数据库。
    def __init__(self, dbName):
        self.name = dbName
        self.con =  sqlite3.connect("moviedbtext.db")
        self.cursor = self.con.cursor()
        try:#todo
            self.cursor.execute('''CREATE TABLE text (Title text, BoxOffice text)''',)
            self.con.commit()
            print("create!")
        except sqlite3.OperationalError:
       	    print("open!")
            pass
    #插入数据
    def  insData(self, dbList):
        self.cursor.execute(dbList[0],dbList[1])
        self.con.commit()
        
    #删除数据   
    def delData(self, dbValue):
        pass
        
    #查询数据
    def selData(self, dbValue):
        return self.cursor.execute(dbValue)
        
    #更新数据
    def updateData(self, dbValue):
        pass
        
    #关闭数据库
    def closeDB(self):
        self.con.close()
        print("close!")


if __name__ == "__main__":
    db = wrappedSQL('text')
    db.closeDB()
