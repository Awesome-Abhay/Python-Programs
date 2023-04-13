# (1, 2, 3, 8, 9, 3, 2, 1) → 3
# (1, 2, 1, 4) → 3
# (7, 1, 2, 9, 7, 2, 1) → 2
import os
os.system("cls")
def isMirrorInverse(arr, n) :  

    for i in range(n) :

        if (arr[arr[i]] != i) :

            return False  

    return True


# if _name_ == "_main_" :

arr = [ 1, 2, 3, 8, 9, 3, 2, 1 ]  

n = len(arr) 

if (isMirrorInverse(arr,n)) :

    print("Yes")

else :

    print("No")