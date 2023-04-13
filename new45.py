# Find the Frequency of the Word ‘the’ in a given Sentence
import os
os.system("cls")
x="The Sun is the only source of light energy of the whole Universe"
x=x.split()
c=0
for i in x:
    if i=="the":
        c+=1
print(c)