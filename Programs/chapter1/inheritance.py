#inheritance 
class Books:
    def __init__(self, author, cost, publication, sold_no, price):
        self.author = author
        self.cost = cost
        self.publication = publication
        self.sold_no = sold_no
        self.price = price

    def get_cost(self):
        print(self.cost, self.author, self.publication, self.sold_no)

class magazine:
    def __init__(self, cost, author, publication, sold_no, price, owner):
        self.cost = cost
        self.author = author
        self.publication = publication
        self.sold_no = sold_no
        self.price = price
        self.owner = owner

    def get_details(self):
            print(self.author, self.cost, self.publication, self.sold_no, self.price,self.owner)


 


B1 = Books("Autheor is: Aron", 234, 2011, 55, 670);

B1.get_cost()
print("printing details of magazine ")
M1 =magazine(author ="Ngugi Wa Thiong'o", cost= 1008, publication= 1990, sold_no= 1000, price= 780, owner="Aron Ayub")
M1.get_details()