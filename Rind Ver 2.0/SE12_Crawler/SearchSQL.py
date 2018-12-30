# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from baseCrawler import *
else:
    from .baseCrawler import *

def SearchMovie(name):
    db = wrappedSQL("./SE12_Data/movie.db")
    searchValue = "Movie like '%"+str(name)+"%'"
    lst = db.SelData(Title='data', Value=searchValue)
    db.CloseDB()
    return lst

'''
def SearchActor(name):
    db = wrappedSQL("movie.db")
    searchValue = "Actor like '%"+str(name)+"%'"
    lst = db.SelData(Title='data', Value=searchValue)
    db.CloseDB()
    return lst
'''

def SearchSQL(name):
    msg = []
    lst = SearchMovie(name)
    if lst != []:
        for item in lst:
            str0 = item['Movie']
            str1 = '票房：'+item['BoxOffice']+'万'
            str2 = '上映日期：'+item['Date']
            str3 = '导演：'+item['Director']
            str4 = '分类：'+item['Category']
            str5 = '演员：'+item['Actor']
            msg.extend([[str0,str1,str2,str3,str4,str5]])
    '''
    else:
        lst = SearchActor(name)
        for item in lst:
            msg.append([item['Movie']])
    '''
    return msg


if __name__ == "__main__":
    print(SearchSQL('复仇者联盟'))