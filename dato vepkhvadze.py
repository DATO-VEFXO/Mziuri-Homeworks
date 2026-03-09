class Ticket:
    def __init__(self,name,price,tickets,language="Geo"):
        self.name=name
        self.price=price
        self.tickets=tickets
        self.language=language
    def __str__(self):
        return f"saxeli {self.name} fasi biletis {self.price} bileti {self.tickets} ena {self.language}"
    def __le__(self,ticket1=10):
        if self.tickets <= ticket1:
            print("pirveli filmis bileti ufro metia")
        else:
            print("meore filmis bileti ufro metia")
class User(Ticket):
    def __init__(self,person,balance,price,tickets,language="Geo"):
        super().__init__(price,tickets,language)
        self.person=person
        self.balance=balance
    def __str__(self):
        return f"myidveli aris {self.person} balansi aris {self.balance}"
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance =+ amount
    def buy_tickets(self,amount,t):
        if self.balance >= amount:
            self.balance = self.balance =- amount
            print("tqven warmatebit iyidet bileti")
        else:
            print("tanxa ara sakmarisia")
        self.tickets = self.tickets =- t
        if t > 0:
            print(f"tqven sheisyidet {t} bileti")
        else:
            print("tqven bileti ar giyidiat")
t1 = Ticket("dato",4,6)
print(t1)
print(t1.__le__())
u1 = User("sandro",50,5,3)
u1.buy_tickets(4,5)
