# Use .transpose() (or .T) to convert a (3,4) matrix into (4,3) — rows become columns.
import numpy as np
np.random.seed(42)
arr = np.random.randint(10,100,size=(3,4))


print("shape = ",arr.shape)
print("New Shape =",arr.T.shape)