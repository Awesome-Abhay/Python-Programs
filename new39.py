# Find the Largest & Smallest Word in a String
import os
os.system("cls")
x="abhay agrawal is a cool boy"
x=x.split()
x=list(x)
smallest=x[0]
largest=x[0]
for i in range(0,len(x)):
    if len(x[i])>len(largest):
        largest=x[i]
    if len(x[i])<len(smallest):
        smallest=x[i]
print("largest:- ",largest)
print("smallest:- ",smallest)