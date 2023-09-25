#plain objects do not know how to compare each other, we can use majic methods to make them learn
#usisng the __str and __repr magicc methods

class Book:
    def __init__(self, tilte, author, price):
        super().__init__()
        self.title = tilte
        self.author = author
        self.price = price
    
#the __eq__method checks for equaliy b2n the 2 objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book with non book ")
        return(self.title == value.title and 
        self.author == value.author and
        self.price == value.price)
    


#the _ge_ established >= relationships with anoather obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare boo to non-book")
        return self.price >= value.price

 # the __it__establishes < relationship with obj 
    
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare book in non-book")
        return self.price < value.price


 



b1 = Book("War now", "Muka Leo", 876)

b2 = Book("The window now", "Mitambo Dio", 345)
b3 = Book("War now", "Muka Leo", 908)


#check equality 
print(b3 < b1)


#check for greater and lesser values

#sort them 

books = [b1, b2, b3]
books.sort()
print([book.title for book in books])

#Explore
#(https://docs.python.org/3/reference/datamodel.html)