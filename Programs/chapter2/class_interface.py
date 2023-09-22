#how to inherit from more than one class
#interface is a type of programming feature that is supported using classes 
#a class makes a promise to provide a capability
from abc import ABC, abstractmethod
class JSONify(ABC):
     @abstractmethod
     def toJSON(self):
          pass


class Graphics(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def CalcArea(self):
            pass

class Circle(Graphics, JSONify):
    def __init__(self, radius) :
        self.radius = radius

    def CalcArea(self):
         return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
         return f"{{\"Circle\" : {str(self.CalcArea())} }}"

class Square(Graphics):
    def __init__(self, side):
        self.side = side
    def CalcArea(self):
         return self.side * self.side
    

# g = Graphics()

c = Circle(7)
print(c.CalcArea)
# s = Square(3)
# print(s.CalcArea)

print(c.toJSON())