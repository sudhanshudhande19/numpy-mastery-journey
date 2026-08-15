#==================Statistics questions:=============================
# Take an array [23, 45, 12, 67, 34, 89, 21]. Find np.mean(), np.median(), np.std(), np.var() — all four, and understand the relationship between std and var (std = sqrt(var)).

import numpy as np

arr = np.array([23,45,12,67,34,89,21])

# find the mean
print("mean =",np.mean(arr))

#find the median
print("median =",np.median(arr))

# find the standard deviation
print("standard deviation =",np.std(arr))

#find the varince
print("varince = ",np.var(arr))