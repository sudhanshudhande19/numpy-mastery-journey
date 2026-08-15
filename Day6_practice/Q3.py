# Try np.cumsum() and np.cumprod() on a 1D array — understand how they build a "running total".

import numpy as np

arr = np.array([23, 45, 12, 67, 34, 89, 21])

print(np.cumsum(arr))

print(np.cumprod(arr))