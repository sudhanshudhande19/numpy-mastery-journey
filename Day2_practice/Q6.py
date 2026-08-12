# Challenge: Given an array, extract elements that are divisible by both 3 AND 5 — using a combined boolean conditio

import numpy as np

arr = np.array([3,5,15,30,25,30,21,10,55,15,36,9,6])


ll = (arr %3 ==0) & (arr %5 ==0)
print(arr[ll])
