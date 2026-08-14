# Take a 2D array, convert it to 1D using both .
# flatten() and .ravel(). Both outputs will look the same, 
# but understand the difference (write it in your 
# README — one returns a copy, the other a view).

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

arr1D = arr.flatten()
print(arr1D)