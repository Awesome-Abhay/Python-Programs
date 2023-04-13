# program to swap first element with last element of a list.
# program to convert list to tuple and tuple to list.
# program to slice a tuple.
# program to reverse a tuple.
# find length of tuple, convert tuple to dictionary.
import os
os.system("cls")
x= input("Enter the list:- ")
x=x.split()
x= (list)(x)
temp= x[0]
x[0]=x[-1]
x[-1]= temp
print(x)
str=""
for i in x:
    str=str+i+" "  # to convert list into string.
print(str)