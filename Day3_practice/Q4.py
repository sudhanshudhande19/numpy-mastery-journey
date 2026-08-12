# Create a (4,3) matrix. Find the mean of each column (axis=0),
# then subtract that mean from each column using broadcasting 
# (this is normalization — used a lot in ML).

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])

print("mean of each Column in Array =")
col_mean = np.mean(arr, axis=0)
print(col_mean)

normalized = arr - col_mean
print("Normalized Array", normalized)
