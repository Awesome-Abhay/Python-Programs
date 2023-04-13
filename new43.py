# Advance concept of list.
import os
os.system("cls")
my_list=[1,2,3,4,5]
squares = [x**2 for x in my_list]
print(squares)  # Output: [1, 4, 49, 100, 25]

evens = [x for x in my_list if x % 2 == 0]
print(evens)  # Output: [2, 10]
