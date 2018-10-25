#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Huang "AAA" Quanzhe'

import requests

class baseCrawler:
    def __init__(self, url):
        self.baseUrl = url
        return
    def getData(self):
        self.r = requests.get(self.baseUrl)
        return self.r
    def displayData(self):
        outputData = self.r.text.split('\n')
        for line in outputData:
            print(line.encode(self.r.encoding))
        return

class baseParser:
    pass

if __name__ == "__main__":
    url = "http://www.baidu.com"
    baidu = baseCrawler(url)
    baidu.getData()
    baidu.displayData()


