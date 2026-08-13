# Take a (5,3) matrix. Get the total column-wise sum using axis=0, 
# then the total row-wise sum using axis=1 — verify that the overall sum is the same both ways.

import numpy as  np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12],
               [13,14,15]])

total_col = np.sum(arr, axis= 0) # sum total column  = 0
total_row = np.sum(arr, axis= 1) # sum total row  = 1

print("Sum of column sums:", np.sum(total_col))
print("Sum of row sums:", np.sum(total_row))
print("Are they equal?", np.sum(total_col) == np.sum(total_row))