# Create Dictionary.
# print the particular key value from the dictionary.
# convert Dictionary to list.
# program to create five student details like name, roll no., subjects, college name, using dictionary.
# how to update values in dictionary using key.
# Which function is used to remove particular key values from the dictionary.--> The Del method is used to remove elements(Values) from the dicitonary.
# How user can apply the loop in dictionary give the suitable example and bring the values of dicitionary.-->
import os
os.system("cls")
details={"Name":"Abhay", "Roll no.":2, "Subjects":["English","Hindi","Computer Science"], "College_Name":"GLA" }
# print(details["Name"])
# details= list(details)
# print(details)
print(details)
d=dict(Name="Jatin")
details.update(d)
print(details)
for i in details.values():
    print(i)