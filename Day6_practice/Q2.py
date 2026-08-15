# Take a (4,4) matrix. Find np.std() with both axis=0 and axis=1 

import numpy as np

np.random.seed(42)
arr =np.random.randint(10,100,size=(4,4))

print(np.std(arr, axis= 0))
print(np.std(arr, axis= 1))