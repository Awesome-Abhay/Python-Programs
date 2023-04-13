# Strong number program. (BUT THERE'S SOME GLITCH)
import os
os.system("cls")
x=int(input("Enter the number:- "))
sum=0
while x!=0:
    remainder= int(x%10)
    for i in range(remainder-1,0,-1):
        remainder=remainder*i
    sum=sum+remainder
    x= int(x/10)
print(sum)