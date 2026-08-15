#=======================Sorting/Searching questions:===========================

# Take an unsorted array [45, 12, 89, 23, 67]. Sort it using np.sort(), and find the indices that would sort it using np.argsort() — understand the difference between the two.

import numpy as np

arr = np.array([[45, 12, 89, 23, 67]])

arr_sort = np.sort(arr)
print("Sort the Array =",arr_sort)

arr_sort_2 = np.argsort(arr_sort)
print("Indices in sort array =",arr_sort_2)