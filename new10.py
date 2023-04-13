# doubt... how can a bool function be False.
import os
os.system("cls")
is_male= input("you are male:- ")
ismale= eval(is_male)
print(ismale)
is_tall= True
if ismale and is_tall:
    print("you are a tall male")
elif ismale and not(is_tall):
    print("you are a short male")
elif not(ismale) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male and not tall")
