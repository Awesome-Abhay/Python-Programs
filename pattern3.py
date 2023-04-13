# *****
# ****
# ***
# **
# *
import os
os.system("cls")
x=int(input("Enter the number:- "))
for i in range(0,x):
    for j in range(x-1-i,-1,-1):
        print("*",end="")
    print()