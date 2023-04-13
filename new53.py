# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True
import os
os.system("cls")
n=int(input("Enter a no:- "))
n1=int(input("Enter another no:- "))
if n==6 or n1==6:
    print("True")
elif abs(n-n1)==6 or abs(n+n1)==6:
    print("True")
else:
    print("False")