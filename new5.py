# Electricity input charges, total bill according to the conditions:- 
# first 50 units= 0.5rs/unit.
# next 100 units= 0.75rs/unit.
# next 100 units= 1.20rs/unit.
# above 250 units= 1.5rs/unit.
# additional surcharge of 20% is added to the bill.
import os
os.system("cls")
x= (int)(input("enter the units:- "))
sum= 0
if x<=50:
    sum= x*0.5
elif x>50 and x<=150:
    sum= 50*0.5 + (x-50)*0.75
elif x>150 and x<=250:
    sum= 50*0.5 + 100*0.75 + (x-150)*1.20
elif x>250:
    sum= 50*0.5 + 100*0.75 + 100*1.20 + (x-250)*1.5
else:
    print("fuck off")
print("charges:- ",sum)
print("+Surcharge:- 20%")
print(sum,"+",x/5,":-",sum+x/5)
sum= sum+ (x/5)
print("total charges:- ",sum,end="")
print("\-only")