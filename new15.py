# Find the Number of Vowels, Consonants, Digits and White space in a String
import os
os.system("cls")
x= input("Enter a string:- ")
v=0
c=0
d=0
s=0
vowels=['a','e','i','o','u']
for i in range(len(x)):
    if x[i] in vowels:
        v+=1
    elif x[i] not in vowels and x[i].isalpha():
        c+=1
    elif not(x[i].isalpha()) and x[i]!=" ":
        d+=1
    elif x[i]==" ":
        s+=1
print("no. of vowels:- ",v)
print("no. of consonants:- ",c)
print("no. of digits:- ",d)
print("no. of whitespaces:- ",s)
