# program to count the element in a list until an element is a tuple.
import os
os.system("cls")
x=[1,"abhay","harshit","jatin",2,3,(1,2),4,5,6]
c=0
for i in x:
    if type(i)!=tuple:
        c+=1
    else:
        break
print(c)