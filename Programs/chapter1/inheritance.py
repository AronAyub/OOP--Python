"""
If you wanna understand inheritance in OOP for python, keenly follow this code,
email at: engaron8@gmail.com for clarifications:
"""
#inheritance 
#define a base class with same attributes:
class Publication:
     def __init__(self, author, price):
          self.author = author
          self.price =  price

"""both Magazine and Newspaper has got country and owner as common attribute
we create a base class for the two attributes"""
class Periodical(Publication): #this base class is inheriting from publication class.
     def __init__(self, author, price, country, owner):
          super().__init__(author, price)
          self.country = country
          self.owner = owner
class Books(Publication):
    def __init__(self, author,price, publication, pages, type):
        #TO MAKE IT inheritance call super class init function
        super().__init__(author, price)
        self.publication = publication
        self.pages = pages
        self.type = type

    def getinfo_books(self):
        print(self.price, self.author, self.publication, self.pages, self.type)

class magazine(Periodical):
    def __init__(self, price, author, public, owner, country):
        super().__init__(author, price, country, owner)
        self.public = public

    def get_info_magazine(self):
        print(self.price, self.author, self.public, self.owner,self.country)

class NewsPaper(Periodical):
     def __init__(self, price, author, private, owner, country):
        super().__init__(author, price, owner, country )
        self.private = private


     def get_info_newspaper(self):
          print(self.price, self.author, self.owner, self.country, self.private)

print("Get Books details: ")
B1 = Books("Author is: Aron, ", "price is: = 100", "published:  2011", "Pages : 55", "Type : Love Book")
B1.getinfo_books()
B2 = Books(author = "Ken walibora", price= 100, publication= 2001, pages = 78, type = "Tamthilia")
B2.getinfo_books()
print()

print("Get magazineinfo: ")
M1 =magazine(author ="Ngugi Wa Thiong'o", price= 780, owner="Aron Ayub", country= "Kenya", public = "True")
M1.get_info_magazine()

print()
print("Newspaper info ")
N1 =NewsPaper(price= 2000, author = "Aron Ayub", private='False', owner= "Chero", country= "Ireland")
N1.get_info_newspaper()

print(B1.publication)
print(B1.pages)
print(B1.price)
print(B1.author)


