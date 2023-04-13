# Sort dictionary by it's values. And use of lambda() function.
import os
os.system("cls")
marks={1:41, 5:10, 3:35, 2:30, 4:18}
mid=int(len(marks)/2)+1
marks= sorted(marks.items(), key= lambda x:x[1])
marks= dict(marks)
print(marks)