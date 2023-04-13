# in tuple there is no need to type parenthesis, it's by default a tuple.
# and in tuple we can't do any operations. Tuple is immutable.
# {}--> set        ()--> tuple         []--> list.
marks=97,93,27,97,97,97 #--> it is a tuple only because there is paranthesis and a list takes square brackets.
print(marks)
#--> we can't do any operation with tuple. like deleting, inseting or appending.
print(marks.count(97)) #--> to count the no. of a particular element.
print(marks.index(97)) #--> to get the index of any no.