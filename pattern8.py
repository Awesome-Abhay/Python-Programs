# *        *
# **      **
# ***    ***
# ****  ****
# **********
import os
os.system("cls")
x=int(input("Enter the number:- "))
for i in range(1,x+1):
    print(i*"*"+(x*2-2-i-i+2)*" "+i*"*")