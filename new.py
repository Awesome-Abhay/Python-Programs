# prime no. program.
def prime(s):
    c=0
    for i in range(2,s):
        if s%i==0:
            c+=1
            break
    if c==0:
        print("prime no.")
    else:
        print((str)(s)+" is not a prime no.")

s=(int)(input("Enter any no. to check if it is prime:- "))
prime(s)
