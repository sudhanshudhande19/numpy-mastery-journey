# Use np.linalg.det() to find the determinant of a (2,2) matrix

import numpy as  np

np.random.seed(42)
arr = np.random.randint(10,100,size=(2,2))

arr2  = np.linalg.det(arr)
print(arr2)