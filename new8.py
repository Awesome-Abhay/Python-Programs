from math import *
import os
os.system("cls")
my_num= 5
your_num= -10
print(abs(your_num)) # to get the absolute value of any num.
print(max(my_num, your_num,6,10,192,192,1,232,34)) # to get the largest one of them.
print(round(3.4)) # to get the roundfigure.
print(floor(5.12345)) # in math function and use to get only the without decimal value.
print(ceil(3.1)) # in math function and use to get a number up.
a= float(input("Enter a number:- "))
b= float(input("Enter another number:- "))
result= a+b
print(result)
friends=["Abhay", "Jatin", "Jaismine", "Jainy"]
numbers=[10,20]
friends.extend(numbers)
print(friends)