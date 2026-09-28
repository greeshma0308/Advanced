# class Account:
#     def __init__(self):
#         self.acctname = input("enter account name:")
#         self.acctnumber = int(input("enter account number:"))
#         self.balance = int(input("enter balance:"))
#     def withdraw(self):
#         amount=int(input("Enter the amount:"))
#         if amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             self.showbalance()
#     def deposit(self):
#         amount = int(input("Enter the amount:"))
#         self.balance+=amount
#         self.showbalance()
#     def showbalance(self):
#         print("current balance:",self.balance)
# l=[]
# while(1):
#     print("1.Create an account")
#     print("2.Withdraw")
#     print("3.Deposit")
#     print("4.Show balance")
#     print("5.Exit")
#     ch = int(input("enter your choice:"))
#     if ch == 1:
#         a=Account()
#         l.append(a)
#     elif ch == 2:
#         accno = int(input("Enter account number: "))
#         for i in l:
#             if i.acctnumber==accno:
#                 i.withdraw()
#                 break
#         else:
#             print("Does not exist")
#     elif ch == 3:
#         accno = int(input("Enter account number: "))
#         for i in l:
#             if i.acctnumber == accno:
#                 i.deposit()
#                 break
#         else:
#             print("Does not exist")
#     elif ch == 4:
#         accno = int(input("Enter account number: "))
#         for i in l:
#             if i.acctnumber == accno:
#                 i.showbalance()
#                 break
#         else:
#             print("Does not exist")
#     else:
#         exit()


class Student:
    def __init__(self):
        self.name=input("Enter name:")
        self.rollno=int(input("Enter roll no:"))
        self.marks=int(input("Enter marks:"))
    def display(self):
        print(self.rollno,self.name,self.marks)
    def update_marks(self):
        self.mark=int(input("Enter new marks:"))

l=[]
while(1):
    print("1.Add Student")
    print("2.Update marks")
    print("3.Display all student details")
    print("4.Search Student by Roll Number")
    print("5.Delete student")
    print("6.Exit")
    ch = int(input("enter your choice:"))
    if ch == 1:
        s=Student()
        l.append(s)
    elif ch == 2:
        roll = int(input("Enter roll number: "))
        for i in l:
            if roll==i.rollno:
                i.update_marks()
                break
        else:
            print("Student not found")
    elif ch == 3:
        for i in l:
                i.display()
    elif ch == 4:
        roll = int(input("Enter roll number: "))
        for i in l:
            if i.rollno == roll:
                print("student found")
                break
        else:
            print("Student not found")
    elif ch == 5:
        roll = int(input("Enter roll number: "))
        for i in l:
            if i.rollno == roll:
                l.remove(i)
                break
        else:
            print("Student not found")
    else:
        exit()
