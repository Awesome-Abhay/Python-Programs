# Fibonacci series.
import os
os.system("cls")
x=int(input("Enter the number:- "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
c=0
while c<x:
    c=a+b
    if c<=x:
        print(c,end=" ")
    a=b
    b=c
