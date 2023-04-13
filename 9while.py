# Star patterns.
import os
os.system("cls")
i=1
while i<=5:
    print(i,end=" ")
    print(i*"*") # if we multiply the number with the string then the string get printed at that times.
    i+=1   # here increment/decrement operator doesn't work in python

# to print more to less stars.(reversed star pattern.)
i=5
while(i>=1):
    print(i,end=" ")
    print(i*"*")
    i-=1