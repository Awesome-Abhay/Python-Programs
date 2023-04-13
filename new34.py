# program to convert tuple to a string.
import os
os.system("cls")
x=(1, 2, 3, 4)
s=""
for i in range(0,len(x)):
    s=s+str(x[i])
print(s)