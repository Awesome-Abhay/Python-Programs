# Palindrome no.
import os
os.system("cls")
x=int(input("Enter the number:- "))
temp=x
sum=0
while x!=0:
    remainder= int(x%10)
    sum= (sum*10)+remainder
    x= int(x/10)
if sum==temp:
    print("Palindrome")
else:
    print("Not")
    