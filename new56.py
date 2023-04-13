# Armstrong no.
import os
os.system("cls")
x=int(input("Enter the number:- "))
temp=x
c=0
while x!=0:
    remainder= int(x%10)
    c+=1                         # This loop is to count the number of digits.
    x=int(x/10)
sum=0
x=temp
for i in range(0,c):
    remainder= int(x%10)
    p=1
    for j in range(0,c):
        p=remainder*p
    sum=sum+p
    x=int(x/10)
if sum==temp:
    print("Armstrong no.")
else:
    print("Not")