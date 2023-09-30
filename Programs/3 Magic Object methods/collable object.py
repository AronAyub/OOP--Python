from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"{self.title}, by {self.author}, cost {self.price}"
    

#call method   can be used to call the object like a function
    def  __call__(self, title, author , price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("The Way", "ayub Loo", 1000)
b2 = Book("The gate", "luke Gure", 300)


print(b1, f"{and b2}")