# Real use case: Take a daily sales array [100, 150, 80, 200, 120], use cumsum() to find the total cumulative sales up to each day.


import numpy as np

arr = np.array([100, 150, 80, 200, 120])

cumulative_sum = np.cumsum(arr)
print("total Cumulative Sum each Day=",cumulative_sum)