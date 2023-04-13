# program to print even no. between 1 to 20 and print in list format.
import os
os.system("cls")
s=""
for i in range(1,21):
    if i%2==0:
        s=s+(str)(i)+" "
s=s.split()
s=(list)(s)
print(s) 
print(*s) # to unzip the elements of a list.