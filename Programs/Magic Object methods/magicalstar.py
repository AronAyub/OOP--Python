#we use them to create strings
#using the __str and __repr __ magic methods

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
#Use the __str___ method to return a string
    def __str__(self):
        return f"Book title is {self.title} by {self.author}, costs {self.price}"

#use __repr__method to return an obj representation
    def __repr__(self):
        return f"Title= {self.title},author={self.author},price={self.price}"
        

b1 = Book("The Kilimu", "Aron", 500)
b2 = Book("What we do", "lin", 100)


print(str(b1))
print(repr(b2))
