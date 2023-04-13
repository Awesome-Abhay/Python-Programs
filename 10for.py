# Star patterns.
import os
os.system("cls")
for item in range(5):
    print(item+1)
for i in range(5):    # "in" is a keyword
    print((i+1)*"*")

# to print reversed triangle.
for i in range(5,0,-1):
    print(i*"*")

# reversed triangle with two "for" loops.
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

