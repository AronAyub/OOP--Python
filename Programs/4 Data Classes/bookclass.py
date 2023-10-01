from dataclasses import dataclass

@dataclass #decorate auatomatically behind the schene initializes the attributes 
class Book:
    title: str
    author: str
    pages: int
    price : float
    

    def __str__(self):
        return f"{self.title}, by {self.author}, pages {self.pages} costs {self.price}"
    

#create some instance 

b1 = Book("Wangwe wa kwiri", "Aron Ayub", 69, 100.78)
b2 = Book("Karura Forst", "Mulio Mario", 104, 66.50)
b3 = Book("Karura Forst", "Mulio Mario", 104, 66.50)

print(b1.__str__())
print(b2.price)

#data classes implement __repr__
print(b2==b3)