# Use np.unique() to remove duplicate values from an array, e.g. [1,2,2,3,3,3,4].

import numpy as np

arr = np.array([1,2,2,3,3,3,4])
arr_unique = np.unique(arr)
print("Unique Value in Array =",arr_unique)
