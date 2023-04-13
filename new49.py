# how many no. are there whose reverse is present in the list
# (1, 2, 3, 8, 9, 3, 2, 1) → 3
# (1, 2, 1, 4) → 3
# (7, 1, 2, 9, 7, 2, 1) → 2
import os
os.system("cls")
x=[1, 2, 3, 8, 9, 3, 2, 1]
reverse=len(x)
for i in range(0,len(x)-1):
    new_x=[]
    for j in range(0,reverse):
        new_x.append(x[j])
    new_x.reverse()
    c=0
    for j in range(0,len(x)-len(new_x)+1):            
        for k in range(0,len(new_x)):
            if new_x[k]!=x[k]:
                c+=1
                break 
    if c<len(x)-len(new_x)+1:
        print(len(new_x))
        break
    reverse-=1