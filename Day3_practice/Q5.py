# Take two arrays with incompatible shapes, 
# like (3,4) and (3,). Try adding them — observe 
# the error and understand why the broadcasting rule fails here.

import numpy as np

arr = np.array([[1,2,3,9],
               [4,5,6,8],
               [7,8,9,10]])

Arr = np.array([1,2,3])
Arr_reshaped = Arr.reshape(3,1)
jj = arr + Arr_reshaped
print(jj)