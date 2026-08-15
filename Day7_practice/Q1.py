# Create two (2,2) matrices and try both element-wise multiplication (*) and matrix multiplication (np.dot() or @) — the results will differ, understand why.

import numpy as np

arr =np.array([[1,2],
              [3,4]])

arr2 = np.array([[5,6],
                [7,8]])

element_arr = arr * arr2
print("element wise multiplication =",element_arr)

matrix_arr = np.dot(arr,arr2)
print("Matrix Multiplication =",matrix_arr)