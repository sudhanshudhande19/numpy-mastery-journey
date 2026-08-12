# Replace all negative numbers in a 2D array with 0 using boolean masking.

import numpy as  np

arr = np.array([[-22,-33],[-44,-55]])
arr[arr < 0] = 0
print(arr)