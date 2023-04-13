# *    
# **   
# ***  
# **** 
# *****
import os
os.system("cls")
x=int(input("enter the no:- "))
# for i in range(0,x):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
for i in range(1,x+1):
    print(i*"*",end="")
    print()