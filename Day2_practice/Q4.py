# Fancy indexing: extract elements at specific indices (e.g. [1,3,5]) from an array in one go.

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

kk= [1,3,5,7]
print(arr[kk])
