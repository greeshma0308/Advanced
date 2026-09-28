# write a program to read a text file and displays the number of lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print("number of lines:",len(s))
# f.close()

#write a program to display the number of words in a file
# f=open('k.txt','r')
# s=f.read()
# words=s.split()
# print("number of words",len(words))
# f.close()

#write a program to update the second line in a file
# f=open('k.txt','r')
# s=f.readlines()
# s[1]='new line'
# f.close()
#
# f=open('k.txt','w')
# f.writelines(s)
# f.close()

#write a program to display the last 5 lines in a file
# f=open("k.txt", "r")
# s=f.readlines()
# print(s[-5:])
# f.close()

#program to search a particular word in a file
# f=open("k.txt", "r")
# s=f.read()
# word=input("Enter the word to search: ")
# if word in s:
#     print("Word found")
# else:
#     print("Not found")
# f.close()

#find the number of letters,digits,and spaces in a file
# f=open("k.txt", "r")
# s=f.read()
# letters=0
# digits=0
# space=0
# for i in s:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
#     elif i.isspace():
#         space+=1
#     else:
#         pass
# print('letters:',letters)
# print("digits:",digits)
# print("spaces:",space)
# f.close()

#reverse the lines in a file
# f=open("k.txt", "r")
# s=f.readlines()
# s=s[::-1]
# f.close()
# f=open("k.txt", "w")
# f.writelines(s)
# f.close()


# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.

f1=open("totalstudents.txt",'r')
total=f1.readlines()
print(total)
f2=open("passedstudents.txt",'r')
passed=f2.readlines()
print(passed)
f3=open("failed_students.txt",'w')
for i in total:
    if i not in passed:
        f3.write(i)
f1.close()
f2.close()
f3.close()