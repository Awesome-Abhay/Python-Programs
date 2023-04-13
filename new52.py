# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0
def caught_speeding(speed, birthday):
    if birthday=="True":
        if speed<=65:
            print("0")
        elif speed>=66 and speed<=85:
            print("1")
        else:
            print("2")
    else:
        if speed<=60:
            print("0")
        elif speed>=61 and speed<=80:
            print("1")
        elif speed>=81:
            print("2")
s=int(input("Enter the speed:- "))
b=input("is it your birthday:- ")
caught_speeding(s,b)