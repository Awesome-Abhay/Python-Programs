# program to find the repeated item of a tuple.
import os
os.system("cls")
x=(1,2,1,2,3,1,3,4,4,5,5,5,6,7)
x=list(x)
for i in range(0,len(x)):
    c=0
    for j in range(i-1,-1,-1):
        if x[j]==x[i]:
            c+=1
            break
    k=0
    if c==0:
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                k+=1
                break
        if k>0:
            print(x[j],end=" ")
            
