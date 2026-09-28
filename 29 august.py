# class Employee:
#     def __init__(self):
#         self.empid=int(input("enter id:"))
#         self.name=input("Enter the name:")
#         self.age=int(input("enter age:"))
#         self.salary=int(input("enter salary:"))
#         self.desig=(input("enter designation:"))
#     def getsalary(self):
#         print("Salary:",self.salary)
#     def showpersonaldetails(self):
#         print("Name:",self.name,"Age:",self.age)
# e=Employee()
# e.getsalary()
# e.showpersonaldetails()


# class Student:
#     def __init__(self):
#         self.rollno=int(input("enter roll no:"))
#         self.name=input("Enter the name:")
#         self.mark1=int(input("enter mark1:"))
#         self.mark2 = int(input("enter mark2:"))
#         self.mark3 = int(input("enter mark3:"))
#     def display(self):
#         print("Roll no:",self.rollno)
#         print("Total marks:",self.mark1+self.mark2+self.mark3)
# s=Student()
# s.display()

# class Book:
#     def __init__(self):
#         self.title=input("enter title:")
#         self.author=input("Enter the author:")
#         self.price=int(input("enter price:"))
#         self.pages=int(input("enter pages:"))
#         self.language=input("Enter the language:")
#     def gettitle(self):
#         print("Title:",self.title)
#     def getauthor(self):
#         print("Author:",self.author)
#     def getprice(self):
#         print("Price:",self.price)
#     def settitle(self):
#         self.title=input('Enter new title:')
#         self.gettitle()
#     def setauthor(self):
#         self.author=input("Enter new author:")
#         self.getauthor()
#     def setprice(self):
#         self.price=int(input("enter new price:"))
#         self.getprice()
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
# b.settitle()
# b.setauthor()
# b.setprice()



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
a1=Account()
a2=Account()
# a.showbalance()
# a.withdraw()
# a.deposit()
# a.showbalance()

l=[a1,a2]
for i in l:
    print(i.acctname)
    i.showbalance()