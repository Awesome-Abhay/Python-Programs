# Find the Largest & Smallest Word in a String
import os
os.system("cls")
x=input("Enter the string:- ")
x= x.split()
largest= x[0]
smallest= x[0]
for i in range(len(x)):
    if len(x[i])>len(largest):
        largest= x[i]
    elif len(x[i])<len(smallest):
        smallest= x[i]
print("largest:- ",largest)
print("smallest:- ",smallest)