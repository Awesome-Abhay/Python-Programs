# Fibonacci series
import os
os.system("cls")
x=0
y=1
c= int(input("enter to which the series is be printed:- "))
print(x," ",y,end="")
z=0
while z<c:
    z=x+y
    x=y
    y=z
    print(" ",z,end="")
    