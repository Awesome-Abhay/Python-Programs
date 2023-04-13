name = "Abhay Agrawal"
print(name.lower())  #--> to change the string into lowercase.
print(name.upper())  #--> to change the string into uppercase.
print(name.find('S')) #--> will return index or -1(for not find)
print(name.find('Agrawal')) #--> output:- 6
print(name.find("A")) #--> Drawback is that it prints only 0 rather it should print 0 and 7.
print(name.find("agrawal")) #--> output:- -1 and can use double quotes also.
print(name.replace("Agrawal", "Goyal")) #--> to replace a string with another.
print(name) #--> output:- Abhay Agrawal, because it doesn't change the original string.
print(name.replace("A","S")) #--> it's going well but not the third one.
print("A" in name) #--> if we don't want to print the index just want to find the character.
print("s" in name) #--> output will be false.
print("Abhay" in name) #--> True
print(name.count("A"))
