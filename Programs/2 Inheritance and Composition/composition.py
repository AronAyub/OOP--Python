#shairing objects attributes and inheritance at the same time
class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        
        self.author = author

        self.chapters = []

    def addchapters(self, chapter):
        self.chapters.append((chapter))
    
    def getbookpagecount(self):
        result = 0
        for chap in self.chapters:
            result += chap.pagecount
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self,name, pagecount ):
        self.name  = name
        self.pagecount = pagecount
            
           
author = Author("Ngugi", "StoryBook")
b1 = Book("River and the the Source", 200.0, "Luo Lady")

b1.addchapters(Chapter('chapter 1', 34))
b1.addchapters(Chapter('chapter 2', 67))

print(b1.title)
print(b1.getbookpagecount())