# Use np.linalg.inv() to find the inverse of a (2,2) matrix, then verify 
# that matrix @ inverse gives (approximately) the identity matrix.

import numpy as np

np.random.seed(42)
arr = np.random.randint(10,100,size=(2,2))

arr2 = np.linalg.inv(arr)
print("matrix inverse =")
print(arr2)
identity_matrix = arr @ arr2
print()
print("identity mtrix =")
print(identity_matrix)