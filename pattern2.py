# *****
#  ****
#   ***
#    **
#     *
import os
os.system("cls")
x=int(input("Enter the number:- "))
for i in range(0,x):
    for j in range(0,i):
        print(" ",end="")
    for j in range(x-i-1,-1,-1):
        print("*",end="")
    print()