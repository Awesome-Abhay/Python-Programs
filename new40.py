# Remove all Characters in Second String which are present in First String
import os
os.system("cls")
x="abcde fghijk"
y="abclm nopqrst"
x=list(x)
y=list(y)
new_y=""
for i in y:
    if i not in x:
        new_y=new_y+i
print(new_y)    