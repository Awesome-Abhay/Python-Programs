import os
os.system("cls")
def addition(a,b):
    sum= a+b
    return(sum)
def subtraction(a,b):
    s= a-b
    return(s)
def multiply(a,b):
    m= a*b
    return(m)
def division(a,b):
    d= a/b
    return(d)
def squareroot(a):
    r= a**0.5
    return(r)
def square(a):
    s= a*a
    return(s)
a= int(input("Enter the number:- "))
b= int(input("Enter another number:- "))
c=multiply(a,b)
print(c)