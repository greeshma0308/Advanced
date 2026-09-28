#create an abstract class shape with abstract method get_area() and get_perimeter().
# create 2 subclass rectangle and sqaure.each class should calculate area and perimeter differently

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter length:"))
#         self.breadth=int(input("Enter breadth:"))
#     def get_area(self):
#         print("Area:",self.length*self.breadth)
#     def get_perimeter(self):
#         print("Perimeter:",2*(self.length+self.breadth))
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("Enter side:"))
#     def get_area(self):
#         print("Area:",self.side*self.side)
#     def get_perimeter(self):
#         print("Perimeter:",4*self.side)
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# s=Square()
# s.get_area()
# s.get_perimeter()


from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self):
        self.name = input("enter name:")
        self.id = int(input("enter id:"))
        self.age = int(input("enter age"))
    @abstractmethod
    def calculate_salary(self):
        pass
class Full_time_employee(Employee):
    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input("Enter salary:"))
    def calculate_salary(self):
        print("salary:",self.monthly_salary)
class Part_time_employee(Employee):
    def __init__(self):
        super().__init__()
        self.hour=int(input("enter hour:"))
        self.rate=int(input("enter rate:"))
    def calculate_salary(self):
        print("salary:",self.hour*self.rate)
f=Full_time_employee()
f.calculate_salary()
p=Part_time_employee()
p.calculate_salary()