# delete duplicacies of the same words in a string.
import os
os.system("cls")
x="I am a a a a a cool cool cool boy"
x = x.split(" ")
length= len(x)
for i in range(length-1):
    if x[i]==x[i+1]:
        for j in range(i,length-1):
            x[j]=x[j+1]
        i-=1
        length-=1
for i in range(length+3):
    print(x[i], end=" ")
