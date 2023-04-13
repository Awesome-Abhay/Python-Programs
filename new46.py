# print the word ending with letter "s"
import os
os.system("cls")
x="Abhyas is the only way to ace your skill"
x=x.split()
for i in x:
    if i[-1]=="s":
        print(i)
