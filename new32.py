# program to check the greatest list between two lists.(using index) if they are equal, print yes.
import os
os.system("cls")
x=input("enter the elements of x:- ")
x=x.split()
y=input("Enter the elements of y- ")
y=y.split()
if len(x)>len(y):
    print("x")
elif len(x)<len(y):
    print("y")
else:
    print("Both are equal")