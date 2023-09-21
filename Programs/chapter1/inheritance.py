#inheritance 
class Books:
    def __init__(self, author, cost, publication, sold_no, price):
        self.author = author
        self.cost = cost
        self.publication = publication
        self.sold_no = sold_no
        self.price = price

    def getinfo_books(self):
        print(self.cost, self.author, self.publication, self.sold_no)

class magazine:
    def __init__(self, cost, author, publication, sold_no, price, owner):
        self.cost = cost
        self.author = author
        self.publication = publication
        self.sold_no = sold_no
        self.price = price
        self.owner = owner

    def get_details_magazine(self):
            print(self.author, self.cost, self.publication, self.sold_no, self.price,self.owner)


class NewsPaper:
     def __init__(self, cost, author, publication, sold_no, price) :
        self.cost = cost
        self.author = author
        self.publication = publication
        self.sold_no = sold_no
        self.price = price


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