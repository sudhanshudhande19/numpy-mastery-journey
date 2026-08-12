# Take a 1D array [1,2,3] and a scalar 5, add them together. Observe how the scalar gets applied to every element (this is the simplest broadcasting example).

import numpy as np

arr = np.array([1,2,3])
hh = arr +5
print(hh)