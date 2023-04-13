# 1
# 12
# 123
# 1234
# 12345
import os
os.system("cls")
x=int(input("Enter the number:- "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    print()