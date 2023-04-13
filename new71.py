import os
os.system("cls")
def sum(a,b):
    c= a+b
    return(c)
def sumofdigits(a):
    s=0
    while(a!=0):
        r= int(a%10)
        s= sum(s,r)
        a= int(a/10)
    return(s)
a= int(input("Enter the number:- "))
b=sumofdigits(a)
print(b)