# Try np.max() and np.min() 
# with both axis=0 and axis=1 — note the shape of the results.

import numpy as np

arr = np.array([[11,22,33,44],
               [55,66,77,88],
               [99,100,200,300],
               [400,500,600,700]])

# MAX
print("Max per column (axis=0) =", np.max(arr, axis=0))
print("Max per row (axis=1) =", np.max(arr, axis=1))

# MIN
print("Min per column (axis=0) =", np.min(arr, axis=0))
print("Min per row (axis=1) =", np.min(arr, axis=1))