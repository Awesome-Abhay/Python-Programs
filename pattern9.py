# **********
# ****  ****
# ***    ***
# **      **
# *        *
import os
os.system("cls")
x= int(input("Enter the number:- "))
c=0
for i in range(x,0,-1):
    print(i*("*")+ c*" "+i*("*"))
    c+=2