# try:
#     n1=int(input("enter number:"))
#     n2=int(input("enter number:"))
#     d=n1/n2
# except ValueError:
#     print("Value error")
# except ZeroDivisionError:
#     print("zero division error")
# else:
#     print("result",d)
# finally:
#     print("done")
#
#
# # write a program that takes a number as input from user and finds the factorial of that number
# # using math.factorial().use a try -except block to handle the value error if user inputs a
# # number/character input
import math
while(1):
    try:
        n1 = int(input("enter number:"))
        print(math.factorial(n1))
        break
    except ValueError:
        print("value error")
    finally:
        print("done")
#using function
def fact():
    try:
        n1 = int(input("enter number:"))
        print(math.factorial(n1))
    except ValueError:
        print("value error")
        fact()
    else:
        pass
fact()
# # Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# # # and division based on user choice. Handle invalid inputs and division by zero using exception handling.
#MY VERSION
# while(1):
#     try:
#         print("1.Addition")
#         print("2.Subtraction")
#         print("3.Multiplication")
#         print("4.Division")
#         ch=int(input("Enter your choice:"))
#         n1 = int(input("Enter first number:"))
#         n2 = int(input("Enter second number:"))
#         if ch==1:
#             print("Result:",n1+n2)
#         elif ch==2:
#             print("Result:",n1-n2)
#         elif ch==3:
#             print("Result:",n1*n2)
#         elif ch==4:
#             print("Result:",n1/n2)
#         else:
#             exit()
#     except ValueError:
#         print("value error")
#     except ZeroDivisionError:
#         print("zero division error")

#MISS VERSION
# while True:
#     try:
#         print('1.Addition')
#         print('2.Subtraction')
#         print('3.multiplication')
#         print('4.Division')
#         print('5.exit')
#
#         n = int(input("Enter choice"))
#         if n in [1,2,3,4]:
#             n1 = int(input("Enter number"))
#             n2 = int(input("Enter number"))
#             s=n1+n2
#             d=n1-n2
#             m=n1*n2
#             q=n1/n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Input")
#     except:
#         print("Error")
#     else:
#
#         if n == 1:
#                 print('Result', s)
#         elif n == 2:
#                 print("Result", d)
#         elif n == 3:
#                 print("Result", m)
#         elif n == 4:
#                 print("Result", q)
#         else:
#             exit()

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not exist
# try:
#     f=open("file1.txt","r")
#     s=f.read()
#
# except FileNotFoundError:
#     print("File does not exist")
#
# else:
#     print(s)
#     f.close()

#Given a Dictionary
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     key=input("Enter a key:")
#     print("Value:",d[key])
#
# except KeyError:
#     print("Key does not exist")