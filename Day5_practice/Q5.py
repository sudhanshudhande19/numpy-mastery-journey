# Create two (2,3) arrays, combine them vertically with np.vstack() and horizontally with np.hstack(). Note the result shapes.

import numpy as  np

arr = np.array([[1,2,3],
               [4,5,6]])
arr2 =np.array([[7,8,9],
                [10,11,12]])

vertical = np.vstack((arr, arr2))
horizontal = np.hstack((arr, arr2))

print("Vertical Stack Shape =",vertical.shape)
print(vertical)
print("Horizatal Stack Shape =",horizontal.shape)
print(horizontal)