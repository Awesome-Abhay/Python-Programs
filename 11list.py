import os
os.system("cls")
marks=[95,96,98, 'Hello'] # --> List which can store all primitive datatypes like array, integer,
# float, character, union, structure etc.
print(marks) #--> to print the list as it is.
print(marks[3]) #--> to print a particular index. or can print the whole list marks.
print(marks[-1]) #--> to print the last value
print(marks[0:2]) #--> to print only required elements of a list.
for score in marks:
    print(score,end=" ")
print("")
marks.append(99) #--> to add any element at last in a list.
print(marks)
marks.insert(4,100) #--> to insert at any index
print(marks)
print(100 in marks) #--> to check whether the no. is present in the list.
print(len(marks)) #--> to print the length of the list.
i=0
while i<len(marks):
    print(marks[i],end=" ")
    i=i+1
print("")
names=["Abhay", "Harshit"]
marks.extend(names)   # to add another list to the prior list.
print(marks)
marks.remove("Hello")  # to remove a particular element from the list.
print(marks)
marks.pop()  # to remove the last element fromt the list.
print(marks)
for i in range(3):
    marks.append(1)
print(marks)
print(marks.count(1)) # to count the occurrences of a particular element.
marks =["Abhay","Jatin","Harshit","Jainy","Jaismine","Harsh","Gupta"]
marks.sort()  # to sort the list in asceding order.
print(marks)
marks.reverse()  # to reverse the elements of a list.
print(marks)
numbers= marks.copy() # to copy a list into new list.
print(numbers)
marks.clear()
print(marks)  #--> to clear all elements of list.