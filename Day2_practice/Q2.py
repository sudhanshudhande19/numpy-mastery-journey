# Create a 2D array (5x5) and extract a specific row and column using slicing.

import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20],
                [21,22,23,24,25]])
print("Row at index 3 =", arr[3])
print("Column at index 3 =", arr[:,3])