# Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
from math import*
import os
os.system("cls")
x= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for i in range(len(x)):
    temp_list= list(x[i])
    temp_list[-1]= float(temp_list[-1])
    temp_list[-1]= temp_list[-1]- int(temp_list[-1])
    x[i]= tuple(temp_list)
sorted_tuple= sorted(x, key=lambda x: x[1])
print(sorted_tuple)