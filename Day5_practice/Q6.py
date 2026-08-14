# Challenge: Create three separate (2,2) arrays. Use np.concatenate() to combine them along both axis=0 and axis=1

import numpy as  np

arr = np.array([[1,2],
               [3,4]])

arr2 = np.array([[5,6],
                 [7,8]])
arr3 = np.array([[9,10],
                 [11,12]])

# axis=0 — vertical stacking (rows increase)
vertical = np.concatenate((arr, arr2, arr3), axis=0)
print("axis=0 (shape", vertical.shape, "):\n", vertical)


# axis=1 — horizontal stacking (columns increase)
horizontal = np.concatenate((arr, arr2, arr3), axis=1)
print("axis=1 (shape", horizontal.shape, "):\n", horizontal)