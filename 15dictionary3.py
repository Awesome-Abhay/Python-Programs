# use of fromkeys method in dictionary.
import os
os.system("cls")
d= dict.fromkeys(["name", "course", "roll no."])
name=input("Enter the name:- ")
course= input("Enter the course:- ")
rollno= input("Enter the roll no.:- ")
d["name"]=name
d["course"]=course
d["roll no."]=rollno
print(d)

# some operators in dictionary
print("name" in d) #--> membership operator "in" checks only for keys.
del d["roll no."]  #--> to delete any key with it's value.
print(d)
d["name"]="Priyanshu"
print(d)
# slicing is not possible in dictionary because dictionary is an unordered form of data type.
# NOTE:- Slicing, concatenation and multiplication operations are not allowed here.
print(len(d)) #--> to count the no. of pairs in a dictionary.
print(isinstance(d, dict)) #--> to check the data type of a variable.
