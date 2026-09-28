# #inheritance
# class Parent():
#     def m1(self):
#         print("in parent class m1")
#
#     def m2(self):
#         print("in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#     pass
# c=Child()
# c.m2()
# c.m1()
#
#
# #inside child we are giving fn
# class Parent():
#     def m1(self):
#         print("in parent class m1")
#
#     def m2(self):
#         print("in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#     def m3(self):
#         print("in child class m3")
# c=Child()
# c.m2()
# c.m1()
# c.m3()
#
# #using same fn name for parent and child
# class Parent():
#     def m1(self):
#         print("in parent class m1")
#
#     def m2(self):
#         print("in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#     def m3(self):
#         print("in child class m3")
#     def m1(self):  #this is given priority (method overriding)
#         print("in child class m1")
# c=Child()
# c.m2()
# c.m1()
# c.m3()

# #using same fn name for parent and child but use super. for calling parent
# class Parent():
#     def m1(self):
#         print("in parent class m1")
#
#     def m2(self):
#         print("in parent class m2")
#
# p=Parent()
# p.m1()
# p.m2()
#
# class Child(Parent):
#     def m3(self):
#         print("in child class m3")
#     def m1(self):  #this is given priority (method overriding)
#         super().m1()
#         print("in child class m1")
# c=Child()
# c.m2()
# c.m1()
# c.m3()


# class Person():
#     def __init__(self):
#         self.name = input("Enter name:")
#         self.age = int(input("Enter age:"))
#     def show(self):
#         print("Name:",self.name,'Age:',self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno = int(input("Enter roll no:"))
#         self.marks = int(input("Enter marks:"))
#
#     def show(self):
#         super().show()
#         print("Rollno:",self.rollno,"Mark:",self.marks)
#
#     def updatemark(self):
#         self.marks = int(input("Enter new marks:"))
#
# s=Student()
# s.show()
# s.updatemark()


# class Category:
#     def __init__(self):
#         self.category_name=input("Enter category name:")
#     def showcategory(self):
#         print("Category:",self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("Enter product name:")
#         self.price=int(input("Enter price:"))
#         self.quantity=int(input("Enter quantity:"))
#
#     def total_price(self):
#         total=self.price*self.quantity
#         print("Total Price:",total)
# p=Product()
# p.showcategory()
# p.total_price()

class Company:
    def __init__(self):
        self.company_name=input("Enter company name:")
        self.location=input("Enter company location:")
    def display_company(self):
        print("Company name:",self.company_name,"Location:",self.location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter id:"))
        self.empname =input("Enter employee name:")
        self.salary= int(input("Enter salary:"))
    def display_details(self):
        self.display_company()
        print("Employee id:",self.empid)
        print("Employee name:", self.empname)
        print("Salary:", self.salary)

    def update_salary(self):
        self.salary = self.salary + self.salary * 0.10
        print("New Salary:", self.salary)

emp = Employee()
emp.display_details()
emp.update_salary()