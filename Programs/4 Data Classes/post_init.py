#using Post Init function in data classes.
#post init function helps us customize additional properties 

from dataclasses import dataclass

@dataclass #decorate auatomatically behind the schene initializes the attributes 
class Book:
    title: str
    author: str
    pages: int
    price : float

    #__post__init function lets us customize additional properties
    #after object has been initialized through built in -in __init
    
    def __post__init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages}, costs {self.price}"
    
    def __post__in
    

#create some instance 

b1 = Book("Wangwe wa kwiri", "Aron Ayub", 69, 100.78)
b2 = Book("Karura Forst", "Mulio Mario", 104, 66.50)
b3 = Book("Karura Forst", "Mulio Mario", 104, 66.50)

# print(b1.__str__())
# print(b2.price)

#data classes implement __repr__
print(b1.description)

