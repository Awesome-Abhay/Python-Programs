# Write a Python program to replace last value of tuples in a list
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
import os
os.system("cls")
x= eval(input("Enter a list:- "))
for i in range(len(x)):
    temp_list= list(x[i])
    temp_list[-1]= 100
    x[i]= tuple(temp_list)
print(x)