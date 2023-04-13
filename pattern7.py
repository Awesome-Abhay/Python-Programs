# 1
# 23
# 456
# 7891
# 23456
import os
os.system("cls")
x=int(input("Enter the number:- "))
k=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(k,end="")
        k+=1
        if k>9:
            k=1
    print()
