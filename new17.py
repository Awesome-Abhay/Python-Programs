# Sort Elements in Lexicographical Order (Dictionary Order)
import os
os.system("cls")
x= input("Enter the string:- ")
x= x.split()
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i].upper()>x[j].upper():
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)
