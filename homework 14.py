class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount > 2500:
            print("2500-s larze met tanxas ver sheitant")
        elif amount <= 0:
            print("shesatani tanxa dadebiti unda iyos")
        else:
            self.balance += amount
            print(f"{amount} wartmatebit sheitanet")
    def withdraw(self,amount):
        if amount <= 0:
            print("gamosatani tanxa dadebiti unda iyos")
        elif amount > self.balance:
            print("ara sakmarisi balansi")
        else:
            self.balance -= amount
            print(f"{amount} wartmatebit gamoitanet")
    def display_balance(self):
        return f"owner: {self.owner} balance is {self.balance}"
b1 = BankAccount(owner="dato", balance=2400)
print(b1.display_balance())
import math
class Shape:
    def describe(self):
        print("i am a Shape")
class Polygon(Shape):
    def __init__(self,*sides):
        self.sides=sides
class Triangle(Polygon):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        self.a=a
        self.b=b
        self.c=c
    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
t1 = Triangle(11,22,33)
t1.describe()
print(t1.calculate_area())