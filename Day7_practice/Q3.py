# Take the transpose of a (3,3) matrix (.T or np.transpose()), then multiply it with the original matrix and see what happens.

import numpy as np

# np.random.seed(43)
# arr = np.random.randint(10,100,size=(3,3))
arr = np.array([[78, 31 ,61],
                [74 ,68 , 27],
                [59 ,26 ,69]])
print("Original Matrix =")
print(arr)
print()
arr2 = np.transpose(arr)
print("Transpose Matrix =")
print(arr2)
print()
print("Maultiply Matrix =")
print(arr @ arr2)
