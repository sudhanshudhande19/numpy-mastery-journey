# Challenge: Take an array of exam scores [55, 78, 42, 90, 63, 38, 71]:
# 1. Sort it and find the top 3 scores
# 2. Use argsort() to find which original index each top 3 score came from
# 3. Use np.where() to find how many students failed (score < 40)

import numpy as np
arr = np.array([55, 78, 42, 90, 20, 38, 71])

# 1. Top 3 scores
top3_scores = np.sort(arr)[-3:]
print("Top 3 scores:", top3_scores)

# 2. Original indices of top 3 scores
top3_indices = np.argsort(arr)[-3:]
print("Original indices of top 3:", top3_indices)

# 3. Failed students (score < 40)
failed_indices = np.where(arr < 40)[0]
print("Number of failed students:", len(failed_indices))