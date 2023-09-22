#base class that defines tempate for other classes to inherit from
#python oob
#Using Abstract base classes to enforce class constraints.
from abc import ABC, abstractmethod
class Graphics(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def CalcArea(self):
            pass

class Circle(Graphics):
    def __init__(self, radius) :
        self.radius = radius

    def CalcArea(self):
         return 3.14 * (self.radius ** 2)

class Square(Graphics):
    def __init__(self, side):
        self.side = side
    def CalcArea(self):
         return self.side * self.side
    

# g = Graphics()

c = Circle(7)
print(c.CalcArea)
s = Square(3)
print(s.CalcArea)
 