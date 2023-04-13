# Some methods or functions of Dictionary.
import os
os.system("cls")
d= dict(name="Abhay", course="Btech")
print(d.keys()) #--> print the list of keys.
for i in d.keys():  #--> here we can simply use "d" only.
    print(d[i], end=" ") #--> to access the every value of a dictionary.
print()
print(d.values())
for i in d.values():
    print(i, end=" ")  #--> to get directly the values.
print()
print(d.items()) #--> prints all of the pairs of dict. in tuple.

d2=d  #--> here only the references are copying not the actual value.
print(d2) #--> d2 is pointing towards the same value of d.
d2["name"]= "priyanshu" #--> if we make any changes in d2 then the value of d will also be changed.
print(d)
d2= d.copy() # so the right method to copy is copy() method.
d2["name"]="Sujata" 
print(d)
print(d2)
d2.clear() #--> to make it empty, not to destroy it.
print(d2)
d3=dict(name="Jatin", father_name="Jagdish Goyal")
d.update(d3)  #--> to make changes or to update the dictionary.
print(d)
print(d.get("course","BCOM")) #--> get() method is used when we don't want error while
# searching value of a particular key. and second argument of get method is default 
# argument. when there is no key given then it prints the default value.
print(d.setdefault("address","Tangra")) #--> same as get() method and additionally better as 
# if the putted key is not present in the dictionary then it also added that key.
print(d.popitem()) #--> to delete the last entered pair.
print(d)
print(d.pop("name")) #--> to delete by key
print(d)
print(d.pop("age"),34) #--> prints the default_value of that particular key.