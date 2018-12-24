# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import csv
import sys
import time

# pip install requests
import requests

import __init__

class baseCrawler:

    """
    爬虫的基类，不同网站的爬虫应继承这个类，重写相应函数。
	使用子类继承自baseCralwler类。
	重写handle()方法，针对不同网站对参数进行处理。
	重写dataParser()方法，针对不同网站对数据进行解析。
    """
    baseURL = ''
    URL = ''
    # db
    csvdatas = []
    payload = {}
    header = {}
    baseheader = {}
    
    def __init__(self, url):
        """
        构造函数，传入url。
        """
        self.baseURL = url
        return
        
    def GetReq(self):
        """
        获取相应Req。
        """
        # time.sleep(0.1)
        if(self.URL== ''):
            self.header = self.baseheader
            self.r = requests.get(self.baseURL, params=self.payload, headers=self.header)
            self.data = self.r.text
        else:
            self.r = requests.get(self.URL, params=self.payload, headers=self.header)
            self.newdata = self.r.text
        return self.r
        
    def DisplayData(self):
        """
        测试函数
        向屏幕输出测试信息
        """
        outputData = self.r.text.split('\n')
        for line in outputData:
            print(line.encode(self.r.encoding))
        return

    def DataParser(self):
        """
        创建一个解析器，子类必须重写该方法。
        """
        raise NotImplementedError("Subclass of baseCrawler must provide a DataParser() method")
    
    def Handle(self, argc,  *argv):
        """
        对参数进行处理，子类必须重写该方法。
        """
        raise NotImplementedError("Subclass of baseCrawler must provide a Handle() method")
        
    def ToCsv(self, filename):
        raise NotImplementedError("Subclass of baseCrawler must provide a ToCsv() method")

    def ToSql(self):
        raise NotImplementedError("Subclass of baseCrawler must provide a ToSql() method")

    def InitSql(self, dbname, table):
        raise NotImplementedError("Subclass of baseCrawler must provide a InitSql() method")



if __name__ == "__main__":
    url = "http://www.baidu.com"
    baidu = baseCrawler(url)
    baidu.GetReq()
    baidu.DisplayData()
