# Create a 5x5 array using np.arange(), then print its .shape, .ndim, .size, and .dtype.

import numpy as np

arr = np.arange(1,26)

ll = arr.reshape((5,5))

print("This is the Array Shape = ",ll.shape)
print("find the Array =",ll.ndim)
print("find the Array Size =",ll.size)
print("Find the Array type =",ll.dtype)
