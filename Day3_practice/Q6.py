# Challenge: Create a (5,5) matrix of random numbers.
#  Divide each row by its own row-max 
# (normalize each row to 0-1 range) — no loops, only broadcasting

import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20],
                [21,22,23,24,25]])

arr_max = np.max(arr, axis=1 , keepdims=True)
kk = arr / arr_max
print(kk)