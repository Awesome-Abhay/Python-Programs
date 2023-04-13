# use of map function and doubt in lambda function.
import os
os.system("cls")
a=[2,4,6,8,10]
def sqr(n):
    return n*n
b= list(map(sqr,a))
for i in b:
    print(i,end=" ")

