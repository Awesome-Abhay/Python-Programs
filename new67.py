import os
os.system("cls")
x="abhay"
x= list(x)
length=len(x)
for i in range(0,length):
    print(i)
    if i==1:
        x.pop(i)
        i-=1
        print(i)
        length-=3
print(x)
print(length)

# here python is unlike c or java, because here we are using range function which shows
# abnormal behaviour like once it is called then it will run the whole program accordingly
