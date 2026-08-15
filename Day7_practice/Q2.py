# Use np.matmul() to multiply a (2,3) matrix with a (3,2) matrix — observe the resulting shape.

import numpy as np

np.random.seed(42)
arr = np.random.randint(1,10,size=(2,3))

arr2 = np.random.randint(1,10,size=(3,2))

print(np.matmul(arr, arr2))