from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

        #the __str__ func is used to return a user friendly string representation of the object.
    def __str__(self):
            return f"{self.title} by {self.author}, costs {self.price}"
        
#getattribute__ called when an attr is retrivesdd
#do not directly access the attr name ow a recursive loop is created 
    def __getattribute__(self, name):
        if name == "price":
              p = super().__getattribute__("price")
              d = super().__getattribute__("_discount")
              return p - (p * d)
        return super().__getattribute__(name)



#__setatt__ called when an attribute value is set. Don't set tje attribute
#directly  here ow, a recursve loop causesa a crash
    def __setattr__(self, name, value):
        if name == "price":
             if type(value) is not float:
                  raise ValueError("The price is not a float ")
        return super().__setattr__(name, value)
    
              


b1 = Book("war began", "Ayub Aloo", 45.9)
b2 = Book("War ends", "lovio Mukilo", 45.90)

# b1.price = 30.5
# print(b1)

b2.price = int(40)
print(b2)
