# the all method and any method return true or false expressions according to the dicitionary values.
# apply shorted method in dictionary.
# Difference between del and clear method in dictionary.
import os
os.system("cls")
v={True, False, True}
x= any(v)
print(x)
y= all(v)
print(y)

#--> All are true, output is true.
#--> All are false, output is false.
#--> 1 true and others are false, output is false.
#--> 1 is false, all are true, output is false.
#--> if empty then output is true