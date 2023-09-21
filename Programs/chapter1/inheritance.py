#inheritance 
#define a base class with same attributes:
class Publication:
     def __init__(self, author, price):
          self.author = author
          self.price =  price

"""both Magazine and Newspaper has got country and owner as common attribute
we create a base class for the two attributes"""
class Periodical:
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
        print(self.price, self.author, self.publication, self.type)

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
          print(self.price, self.author, self.owner, self.country)



print("Get Books details: ")
B1 = Books("Autheor is: Aron", 234, 2011, 55, 670);
B1.getinfo_books()
print()

print("Get magazineinfo: ")
M1 =magazine(author ="Ngugi Wa Thiong'o", owner= "Mutuku", sold_no= 1000, price= 780, owner="Aron Ayub")
M1.get_details_magazine()

print()
print("Newspaper info ")
N1 =NewsPaper(author = "Aron Ayub", owner ='Karanja', sold_no = 2, price = 1950)
N1.get_info_newspaper()

#creating inheritance is esssential when classes share attributes,
