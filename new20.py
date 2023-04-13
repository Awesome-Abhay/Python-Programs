# ways to access a particular character of a string.
import os
os.system("cls")
x= input("Enter the string:- ")
# y= input("Enter another string:- ")
# for i in range(len(x)):
#     if x[i]==y[i]:
#         y= y[0:i]+"0"+y[i+1:]   # Slicing.
# print(y)
x= x.split()
print(x[1][1])