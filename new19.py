# Anagram
import os
os.system("cls")
x= input("Enter a sting:- ")
x= x.replace(" ","")
x= x.upper()
x= list(x)
y= input("Enter another string:- ")
y= y.replace(" ","")
y= y.upper()
y= list(y)
temp=0
if len(x)==len(y):
    for i in range(len(x)):
        c=0
        for j in range(len(y)):
            if x[i]==y[j]:
                y[j]="0"
                c+=1
                break
        if c==0:
            temp+=1
    if temp>0:
        print("Not Anagram")
    else:
        print("Anagram")
else:
    print("Not Anagram")
