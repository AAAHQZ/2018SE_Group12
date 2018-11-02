#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import requests

#爬虫的基类，不同网站的爬虫应继承这个类，重写相应函数。
class baseCrawler:

#构造函数，传入url。
    def __init__(self, url):
        self.baseUrl = url
        return
        
#获取相应Req。
    def getReq(self):
        self.r = requests.get(self.baseUrl)
        return self.r
        
#输出数据
    def displayData(self):
        outputData = self.r.text.split('\n')
        for line in outputData:
            print(line.encode(self.r.encoding))
        return
     
#创建一个解析器，子类必须重写该方法。
#todo
    def createParser(self):
        raise NotImplementedError("Subclass of baseCrawler must provide a handle() method")
    
#对参数进行处理，子类必须重写该方法。
    def handle(self, *args, **option):
        raise NotImplementedError("Subclass of baseCrawler must provide a handle() method")
        

if __name__ == "__main__":
    url = "http://www.baidu.com"
    baidu = baseCrawler(url)
    baidu.getReq()
    baidu.displayData()


