import os
os.system("cls")
d=dict(name="ram",age=29, salary=35000) # using dict() method we don't need to put colon.
print(d)                # and also don't need to write key in inverted commas.
s=[[1,2],[3,4]]  #--> can be converted into dict.
s= dict(s)
print(s)
sk=dict(zip((1,2,3),(10,20,30))) #--> zip method to make dict.
print(sk)
studentdetails=dict(zip(["name","course","roll no."],["Abhay","Btech","2"]))
print(studentdetails)
sd=dict.fromkeys(('h','e'),(2,3))
m=dict.fromkeys("hello",2)   #--> from keys method to make dictionary.\
print(sd)
print(m)
