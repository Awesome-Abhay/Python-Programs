# slicing and use of format keyword
import os
os.system("cls")
x= "Abhay, is an enthusiastic person of \"{}\" years old"
print(x)
print(x[14:17])  # print in this range.
print(x[:7]) # print from starting.
print(x[6:]) # print to end.
print(x[-12:]) # negative slicing.
print(x.replace("A","Z"))
print(x.split(","))
print(x) # anything from above doesn't change the original string.
print(x.format(12)) # to add any integer no. between the string.
