# to count the elements in a list until an element is a tuple.
import os
os.system("cls")
x= [1,2,3,(4,5,6),4,5,6]
c=0
for i in x:
    if isinstance(i, tuple):
        break
    else:
        c+=1
print("The no. of elements is:- ",c)