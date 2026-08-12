# 2. Create 4x4 arrays using np.zeros(), np.ones(), and np.full() — with three different fill values.
import numpy as np

arr4d = np.array([4,4])

zero = np.zeros(arr4d)
print(zero)
print()
print(np.ones(arr4d))
print()
print(np.full(arr4d,4))