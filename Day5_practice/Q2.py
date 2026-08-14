# Reshape the same 12-element array into shape (2,2,3) — observe what a 3D array looks like.

import numpy as np

arr = np.arange(12)
print(arr.reshape((2,2,3)))