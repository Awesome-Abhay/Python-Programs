# cigar party
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True
import os
os.system("cls")
def cigar_party(n, weekend):
    if weekend=="True":
        if n>=40:
            print("True")
        else:
            print("False")
    else:
        if n>=40 and n<=60:
            print("True")
        else:
            print("False")
n=int(input("enter the no. of cigars:- "))
weekend=input("is it weekend(True/False):- ")
cigar_party(n, weekend)
        

