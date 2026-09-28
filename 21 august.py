# f=open("k.txt",'a')
# f.write('python')
# f.close()
import ftplib


#WAP TO APPEND THE CONTENTS FROM ONE FILE INTO ANOTHER TEXT FILE
# f=open("file1.txt",'r')
# s=f.read()
# f.close()
# f=open("file2.txt",'a')
# f.write(s)
# f.close()

#append and read
# f=open("k.txt",'a+')
# print("first position:",f.tell())
# f.write('python')
# f.seek(0)
# s=f.read
# print(s)

#to delete a file
# import os
# os.remove('k.txt')
# print('file is removed')


#menu driven
def file_read():
    filename = input("enter filename:")
    f = open(filename, 'r')
    s = f.read()
    print(s)
    f.close()

def file_write():
    filename = input("enter filename:")
    f = open(filename, 'w')
    content=input("enter the content:")
    f.write(content)
    f.close()

def file_append():
    filename = input("enter filename:")
    f = open(filename, 'a')
    content = input("enter the content:")
    f.write(content)
    f.close()

def file_search():
    filename = input("enter filename:")
    f = open(filename, 'r')
    s = f.read()
    word = input("Enter the word to search: ")
    if word in s:
        print("Word",word,"is present")
    else:
        print("word",word,"is absent")
    f.close()

def file_remove():
    import os
    filename = input("enter filename:")
    os.remove(filename)
    print("file",filename,"is deleted")


while(1):
    print("1.File read")
    print("2.File write")
    print("3.File append")
    print("4.File search")
    print("5.File delete")
    print("6.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    else:
        exit()