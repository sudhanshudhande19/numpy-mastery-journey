# Create a (3,3) 2D array and add a (3,) 1D array to it. Observe the result — see how the 1D array broadcasts across every row.
import numpy as  np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
D1_arr = np.array([1,2,3])

Arr = arr + D1_arr
print(Arr) 