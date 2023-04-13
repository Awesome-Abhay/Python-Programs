# find mid element of dictionary.
import os
os.system("cls")
# details={"Name":"Abhay","Roll":"2","College":"GLA"}--> this way, we can't.
details={1:"Abhay", 2:"Harsh",3:"Jatin",4:"Abhinav",5:"Akash"}
print(len(details))
mid= (len(details)//2)+1
print(details[mid])
