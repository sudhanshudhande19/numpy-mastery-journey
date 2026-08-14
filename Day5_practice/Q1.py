# Create a 1D array of 12 numbers (np.arange(12)), convert it to shape (3,4) and (4,3) using .reshape(). Look at both outputs.

import numpy as np

arr = np.arange(12)

print(arr.reshape((3,4)))
print("===================")
print(arr.reshape((4,3)))