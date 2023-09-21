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
        print(self.cost, self.author, self.publication, self.sold_no)

class magazine:
    def __init__(self, price, author, publication, owner, country):
        self.price = price
        self.author = author
        self.publication = publication
        self.owner = owner
        self.country = country

    def get_details_magazine(self):
            print(self.author, self.cost, self.publication, self.sold_no, self.price,self.owner)


class NewsPaper:
     def __init__(self, price, author, publication, owner, country) :
        self.price = price
        self.author = author
        self.publication = publication
        self.price = price
        self.owner = owner
        self.country = country

     def get_info_newspaper(self):
          print(self.cost, self.author, self.publication, self.sold_no, self.price)

print("Get Books details: ")
B1 = Books("Autheor is: Aron", 234, 2011, 55, 670);
B1.getinfo_books()
print()

print("Get magazineinfo: ")
M1 =magazine(author ="Ngugi Wa Thiong'o", cost= 1008, publication= 1990, sold_no= 1000, price= 780, owner="Aron Ayub")
M1.get_details_magazine()

print()
print("Newspaper info ")
N1 =NewsPaper(cost=678, author = "Aron Ayub", publication ='1945', sold_no = 2, price = 1950)
N1.get_info_newspaper()

#creating inheritance is esssential when classes share attributes,
