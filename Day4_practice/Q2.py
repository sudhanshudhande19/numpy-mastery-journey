# On the same matrix, find mean(axis=0) and mean(axis=1) — understand
# which axis gives "average of each column" and which gives "average of each row".

import numpy as np

arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

jj = np.mean(arr , axis= 0, keepdims= True)
print("Find the Mean in Array Column =")
print(jj)

kk = np.mean(arr, axis= 1,keepdims= True)
print("Finde Teh Mean in Array Row =")
print(kk)