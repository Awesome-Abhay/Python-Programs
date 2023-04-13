import os   #--> dictionary do not allow duplicate keys.
os.system("cls")
marks ={"chemistry":98, "maths":95,"english":99} #--> Dictionary
print(marks["maths"])
information={"Ram":"balkishan","Abhay":"Shyam Bihari Agrawal","Jatin":"Jagdish"}
print(information["Abhay"])
marks["physics"]=87 #--> to add any data to dictionary.
print(marks)
marks["physics"]=99 #--> to change the value of any element.
print(marks) #--> we use '\' to write on next line. but it's optional.
months={"Jan":"January",\
        "Feb":"February","Mar":"March",\
        "Ap" :"April",\
        "Ma" :"May",\
        "Jun":"June",\
        "Jul":"July",\
        "Aug":"August",\
       "Sept":"September",\
        "Oct":"October",\
        "Nov":"November",\
        "Dec":"December"}
print(months["Feb"])
print(months.get("Jan","Not a valid Value")) # we can use get function too.
print(months.get("Suv","Not a valid value"))

# dic={1:2, 3:4, 5:6}  #--> it's obviously a dictionary
# a={}  #--> it will be a dictionary as there are only curly brackets.
# b={1,2,3}   #--> since colon is absent, it will act as set.
# print(type(dic))
# print(type(a))
# print(type(b))
