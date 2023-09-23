#how to inherit from more than one class

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()
    
    def display(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
    
c = C()
c.display()

#the python does method resolution order for an attribute and gives 
#the first one a priority
#the other resolution is

print(C.__mro__)
