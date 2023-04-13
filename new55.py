# Perfect no.
import os
os.system("cls")
x=int(input("Enter the number:- "))
sum=0
for i in range(1,x):
    if x%i==0:
        sum=sum+i
if sum==x:
    print("Perfect no.")
else:
    print("Not")
