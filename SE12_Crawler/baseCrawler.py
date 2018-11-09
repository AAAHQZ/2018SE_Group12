#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import requests

#爬虫的基类，不同网站的爬虫应继承这个类，重写相应函数。
class baseCrawler:

    """
	使用子类继承自baseCralwler类。
	重写handle()方法，针对不同网站对参数进行处理。
	重写dataParser()方法，针对不同网站对数据进行解析。
    """

    URL= ''
    
#构造函数，传入url。
    def __init__(self, url):
        self.baseURL = url
        return
        
#获取相应Req。
    def getReq(self):
        if(self.URL== ''):
            self.r = requests.get(self.baseURL)
        else:
            self.r = requests.get(self.URL)
        self.data = str(self.r.text)
        return self.r
        
#向屏幕输出信息
    def displayData(self):
        outputData = self.r.text.split('\n')
        for line in outputData:
            print(line.encode(self.r.encoding))
        return
        
#封装的SQL操作
#todo
    def SQLop(self):
        pass
     
#创建一个解析器，子类必须重写该方法。
    def dataParser(self):
        raise NotImplementedError("Subclass of baseCrawler must provide a handle() method")
    
#对参数进行处理，子类必须重写该方法。
    def handle(self):
        raise NotImplementedError("Subclass of baseCrawler must provide a handle() method")
        

if __name__ == "__main__":
    url = "http://www.baidu.com"
    baidu = baseCrawler(url)
    baidu.getReq()
    baidu.displayData()

