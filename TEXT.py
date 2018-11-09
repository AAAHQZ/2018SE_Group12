import re
obj = re.search('www.(.*).com','5555www.baidu.com1231', re.I|re.M)
print(obj.group())
