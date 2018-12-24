from SE12_Crawler import *

def SearchMovie(name):
    db = wrappedSQL("movie.db")
    searchValue = "Movie like '%"+str(name)+"%'"
    lst = db.SelData(Title='data', Value=searchValue)
    db.CloseDB()
    return lst


def SearchActor(name):
    db = wrappedSQL("movie.db")
    searchValue = "Actor like '%"+str(name)+"%'"
    lst = db.SelData(Title='data', Value=searchValue)

    db.CloseDB()
    return lst

if __name__ == "__main__":
    print(SearchMovie('红海'))
    print(SearchActor('吴京'))