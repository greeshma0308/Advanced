#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.

class Circle:
    def __init__(self):
        self.radius=int(input("enter the radius:"))
    def getarea(self):
        area=3.14*self.radius*self.radius
        print("area:",area)
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print("perimeter:",perimeter)
c=Circle()
c.getarea()
c.getperimeter()


# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.acctname=input("enter account name:")
        self.acctnumber= int(input("enter account number:"))
        self.balance=int(input("enter balance:"))
    def withdraw(self):
        amount=int(input("Enter the amount:"))
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            self.showbalance()
    def deposit(self):
        amount = int(input("Enter the amount:"))
        self.balance+=amount
        self.showbalance()
    def showbalance(self):
        print("current balance:",self.balance)
a=Account()
a.showbalance()
a.withdraw()
a.deposit()
a.showbalance()