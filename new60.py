# Whether it is a part of fibonacci series.
import os
os.system("cls")
x=int(input("Enter the number:- "))
a=0
b=1
c=0
k=0
while c<=x:
    c=a+b
    if c==x:
        print("Yes")
        k+=1
        break
    a=b
    b=c
if k==0:
    print("No")