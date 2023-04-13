# ([1, 2, 4, 6], [2, 4]) → true // if all the elements of x[1] are present in x[0]
import os
os.system("cls")
x=([1, 2, 4, 6], [2,4,6,1,4,2,1,5])
c=0
temp=0
for i in range(0,len(x[1])):
    c=0
    for j in range(0,len(x[0])):
        if x[1][i]==x[0][j]:
            c+=1
            break
    if c==0:
        print("false")
        break
    else:
        temp+=1
if temp==len(x[1]):
    print("true")