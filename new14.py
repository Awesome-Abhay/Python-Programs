# Find the Frequency of Characters in a String
import os
os.system("cls")
x= input("enter a string:- ")
for i in range(len(x)):
    occurrences=0
    again=0
    for k in range(i-1,-1,-1):
        if x[i]==x[k]:
            again+=1
            break
    if again==0:
        for j in range(len(x)):
            if x[i]==x[j]:
                occurrences+=1
        print(x[i],"=",occurrences)
