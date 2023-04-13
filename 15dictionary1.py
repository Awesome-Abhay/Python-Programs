# nested dicionary.
import os
os.system("cls")
d={"Apple":{"Monday":25,"Tuesday":20},
   "Banana":{"Monday":35, "Tuesday":30}}
a={"Name":("Abhay","Jatin","Harshit","Jaismine"), "Class":[2,3,4,5]}
print(d["Apple"]["Tuesday"])
print(d["Banana"])
print(a["Name"][2])
print(a["Class"][0])
d["Apple"]="Apples are my favourite"  #--> Dictionary's values are mutable.
print(d["Apple"])                     #--> But Keys are immutable.
print(d)  #--> whole dictionary has changed
#--> in a dictionary key can be any immutable datatype. Any mutable datatype isn't allowed.

ab={(1,2,3):"Abhay"}  #--> as tuple is immutable so we can use it as a key.
print(ab)
# as={[1,2]:"Abhay"} --> this will show an error because lists are mutable.
an={"a":"abhay", "a":"priyanshu"} #--> it is not allowed.
print(an)
