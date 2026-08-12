# Boolean indexing: extract all numbers greater than 50 from an array, without using a loop.

import numpy as  np
arr =np.array([10,12,55,88,99,44,77,33,96,589,441,63,36,89,50,55,20,])

num = arr > 50
print("find the Greater the 50 in Array")
print(arr[num])
