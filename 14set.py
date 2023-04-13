import os
os.system("cls")
person ={84, 83, 34, 84, 34} #--> a set which holds only unique elements.
print(person) #--> a set has no index, it doesn't know that which value is at which place.
marks={95,98,97,97,97}   #--> so we can say that sets are unordered.
print(marks)
for score in person:
    print(score, end=" ")
print()
# How to make an empty set.
a={}
print(type(a))
a=set()  #--> we use set() method to make an empty set.
print(type(a))