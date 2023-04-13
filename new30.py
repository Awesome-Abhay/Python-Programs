# reverse a list using slicing function.
import os
os.system("cls")
x=[1,2,3,4,5]
# length= len(x)-1
# for i in range(0,int(length/2)):
#     temp= x[i]
#     x[i]=x[length-i]
#     x[length-i]= temp
# print(x)
x= list(reversed(x))
print(x)