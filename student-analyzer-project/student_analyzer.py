import numpy as np

# 1. Generate random marks: 10 students, 5 subjects
np.random.seed(42)  # reproducible results ke liye
marks = np.random.randint(30, 100, size=(10, 5))

# 2. Student-wise total and average
student_total = np.sum(marks, axis=1)
student_avg = np.mean(marks, axis=1)

# 3. Subject-wise average (class performance per subject)
subject_avg = np.mean(marks, axis=0)

# 4. Topper and weakest student
topper_idx = np.argmax(student_total)
weakest_idx = np.argmin(student_total)

# 5. Fail students (average < 40)
fail_mask = student_avg < 40
failed_students = np.where(fail_mask)[0]

# 6. Grade assignment
grades = np.where(student_avg >= 80, 'A',
          np.where(student_avg >= 60, 'B',
          np.where(student_avg >= 40, 'C', 'D')))

# Print report
print("Student Averages:", student_avg)
print("Subject Averages:", subject_avg)
print(f"Topper: Student {topper_idx} with {student_total[topper_idx]} marks")
print(f"Weakest: Student {weakest_idx}")
print("Failed Students (indices):", failed_students)
print("Grades:", grades)