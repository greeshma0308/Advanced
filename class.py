# #static
# class person:
#     def __init__(self,n,a):   #used to initialize obj properties
#         self.name=n
#         self.age=a
#     def show(self):
#         print(self.name,self.age)
# p1=person('arun',23)
# p1.show()
# p2=person('aman',20)
# p2.show()

#dyamic
class person:
    def __init__(self):   #used to initialize obj properties
        self.name=input("Enter the name:")
        self.age=int(input("enter age:"))
    def show(self):
        print(self.name,self.age)
p1=person()
p1.show()
p2=person()
p2.show()