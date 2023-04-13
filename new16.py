# Remove all Characters in a String except alphabet
import os
os.system("cls")
x= input("enter a string:- ")
for i in range(len(x)):
    if x[i].isalpha() or x[i]==" ":
        print(x[i],end="")