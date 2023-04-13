# Find the Frequency of Characters in a String
import os
os.system("cls")
x="abhay agrawal"
for i in range(0,len(x)):
    c=0
    k=0
    for j in range(i-1,-1,-1):
        if x[i]==x[j]:
            k+=1
            break
    if k==0:
        for j in range(i,len(x)):
            if x[i]==x[j]:
                c+=1
        print(x[i]+"="+str(c))
    