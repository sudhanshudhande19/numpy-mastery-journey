# Use np.argmax() and np.argmin() to find the index of the largest number in each row (axis=1).

import  numpy as np

arr = np.array([[1,2,3,4],
               [99,6,7,8],
               [9,10,66,12],
               [13,55,15,16]])

print(np.argmax(arr, axis= 1)) 

print(np.argmin(arr, axis= 1))