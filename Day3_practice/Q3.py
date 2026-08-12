# Take a (3,1) column array and a (1,3) row array, add them together. Observe how it produces a (3,3) matrix — this is "outer broadcasting."
import numpy as np

arr  = np.array([[1],[2],[3]])
Arr = np.array([1,2,3])

total = arr + Arr
print(total)
print(np.prod(total))