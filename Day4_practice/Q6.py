# Challenge: Take a (3,4) matrix representing student marks (3 students, 4 subjects). Find:
# Each student's total and average marks (axis=1)
# Each subject's total and average marks (axis=0)
# Which student scored the highest total marks (using argmax)

import numpy as np

arr = np.array([[60,65,70,90],
                [80,85,90,78],
                [60,80,95,83]])

stu_total = np.sum(arr, axis=1, keepdims=True)
stu_total_avg = stu_total / arr.shape[1]
print("Student totals:\n", stu_total)
print("Student averages:\n", stu_total_avg)

sub_total = np.sum(arr, axis=0, keepdims=True)
sub_total_avg = sub_total / arr.shape[0]
print("Subject totals:\n", sub_total)
print("Subject averages:\n", sub_total_avg)

print("Top student index:", np.argmax(stu_total))