# Create a (4,4) matrix. Find sum(axis=0) and sum(axis=1) — observe the difference between row-wise sum and column-wise sum.

import numpy as  np

arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

jj  = np.sum(arr, axis=0, keepdims= True )
print("Find the sum OF Array Column")
print(jj)

kk = np.sum(arr, axis= 1, keepdims= True)
print("Find the Sum of Array Row")
print(kk)