# Copy vs View Challenge:
# 1. Create an array, then slice it into a new variable (b = a[1:4])
# 2. Change a value in b, then print a — did a change too?
# 3. Now repeat using .copy() (b = a[1:4].copy()) — does a change this time?
# 4. Note the difference in your README

import numpy as  np

np.random.seed(42)
arr = np.random.randint(10,100,size=(4,4))
print("Original Matirx =")
print(arr)
print()
# Create an array, then slice it into a new variable (b = a[1:4])
print("print the array only 1 to 4 row =")
b = arr[1:4]
print(b)
print("==============================")
# Change a value in b, then print a — did a change too?
jj = int(input("enter the value in b, then print a — did a value change too?"))
b[0,1] = jj
print(arr)
print("==============================")
# Now repeat using .copy() (b = a[1:4].copy()) — does a change this time?

# Now repeat using .copy()
b = arr[1:4].copy()
print("Before modifying b (copy):")
print(arr)

kk = int(input("Enter value to change in b (copy version): "))
b[0,1] = kk
print("After modifying b (copy) — check if arr changed:")
print(arr)
print("b:")
print(b)