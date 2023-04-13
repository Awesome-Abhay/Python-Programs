# Delete All Repeated Words in String
import os
os.system("cls")
x="Abhay Abhay is is is is a cool a cool is boy Abhay boy"
x=x.split()
y=[]
for i in x:
    if i not in y:
        y.append(i)
new_x=""
for i in y:
    new_x=new_x+i+" "
print(new_x)