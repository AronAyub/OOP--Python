

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))
@dataclass
class Book:

    title: str   = "Title one thousand"
    author: str = " Alluo Tata"
    pages: int = 70
    print: float = field(default_factory = price_func)


b1 = Book("Wangwe wa kwiri", "Aron Ayub",  100)
b2 = Book("Karura Forst", "Mulio Mario", 104, 66.50)
b3 = Book("Karura Forst", "Mulio Mario", 104, 66.50)


print(b1)
