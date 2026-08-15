# Use np.where(arr > 50) to find which indices have values greater than 50 (you used this in Day 4/the project — revise it here).

import numpy as np

arr = np.array([40,80,90,60,30,50,70,10])

arr_index = np.where(arr > 50)
print(arr_index)