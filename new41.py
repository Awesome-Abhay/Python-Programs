# Reverse the characters input no. of times.
# input--> 2 then output--> ayabh
# input--> 3 then output--> hayab
import os
os.system("cls")
x="abhay"
x=list(x)
y=int(input())
length=len(x)-y
z=""
for i in range(-y,0):
    z=z+x[i]
for i in range(0,length):
    z=z+x[i]
print(z)