# 1.Create a class named Movie with attributes moviename,year,language,director,rating and methods display_details() and update_rating()
class Movie:
    def __init__(self):
        self.moviename=input("Enter movie name:")
        self.year=int(input("Enter year:"))
        self.language=input("Enter language:")
        self.director=input("Enter director name:")
        self.rating=int(input("Enter rating:"))
    def display_details(self):
        print("Movie Name:",self.moviename)
        print("Year:",self.year)
        print("Language:",self.language)
        print("Director:",self.director)
        print("Rating:",self.rating)
    def update_rating(self):
        self.rating=int(input("Enter new rating:"))
m=Movie()
m.display_details()
m.update_rating()
m.display_details()


#2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

class Vehicle:
    def __init__(self):
        self.brand=input("Enter brand:")
        self.model=input("Enter model:")
        self.color=input("Enter color:")
        self.year=int(input("Enter year:"))
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Year:",self.year)
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage = int(input("Enter mileage:"))
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Year:",self.year)
        print("Mileage:",self.mileage)
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc = int(input("Enter CC:"))
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Year:",self.year)
        print("CC:",self.cc)
c=Car()
b=Bike()
c.display()
b.display()