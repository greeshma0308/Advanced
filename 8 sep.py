# try:
#     n1=int(input("enter number:"))
#     n2=int(input("enter number:"))
#     d=n1/n2
# except ZeroDivisionError as z:
#     print(z) #-->system generated msg will be shown
# except Exception as b:
#     print(b)
#     print(type(b)) #gives type of error that occured
# else:
#     print("result",d)
# finally:
#     print("done")

#
# try:
#     n= int(input("enter age:"))
#     if(n<18):
#         raise ValueError("not eligible for voting")
#     else:
#         print("eligible")
# except ValueError as e:
#     print(e)


#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
# try:
#     n= int(input("enter number:"))
#     if(n<=0):
#         raise ValueError("Number must be positive")
#     else:
#         print(n)
# except ValueError as e:
#     print(e)

#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a custom exception InvalidPasswordError with the message ("Password should be 8 characters")
# class InvalidPasswordError(Exception):
#     pass
# try:
#     n= input("enter password:")
#     if(len(n)<8):
#         raise InvalidPasswordError("Password should be 8 characters")
#     else:
#         print("valid password")
# except InvalidPasswordError as e:
#     print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class InsufficientBalanceError(Exception):
    pass
try:
    balance=10000
    amount=int(input("Enter amount:"))
    if amount>balance:
        raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Successful")
except InsufficientBalanceError as e:
    print(e)
