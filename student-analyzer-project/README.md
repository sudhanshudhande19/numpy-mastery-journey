# 📊 Student Performance Analyzer

A NumPy-based mini project that analyzes student marks data — built to bring together everything learned in Day 1-4 (array creation, indexing, boolean masking, broadcasting, and axis operations) into one real-world-style application.

## 📌 Overview

The script generates random marks for **10 students across 5 subjects** and analyzes the data to produce a performance report — student totals/averages, subject-wise class averages, top/weakest performers, failing students, and letter grades.

## 🚀 What It Does

- Generates a random marks dataset (10 students × 5 subjects)
- Calculates each **student's total and average** marks
- Calculates each **subject's class-wide average**
- Identifies the **topper** and the **weakest student**
- Flags **failing students** (average below 40)
- Assigns **letter grades (A/B/C/D)** based on average marks

## 🧠 NumPy Concepts Used

| Concept | Function(s) | Purpose |
|---|---|---|
| Reproducible randomness | `np.random.seed()` | Same random output every run |
| Array generation | `np.random.randint()` | Create the marks dataset |
| Axis operations | `np.sum(axis=1)`, `np.mean(axis=1)` | Per-student total/average |
| Axis operations | `np.mean(axis=0)` | Per-subject class average |
| Index of extremes | `np.argmax()`, `np.argmin()` | Find topper and weakest student |
| Boolean masking | `student_avg < 40` | Identify failing students |
| Conditional indices | `np.where(condition)` | Get indices of students who failed |
| Conditional assignment | `np.where(condition, a, b)` (nested) | Assign grades based on average |

## 💻 How to Run

```bash
python student_analyzer.py
```

## 📄 Sample Output

```
Student Averages: [62.4 71.8 45.2 ...]
Subject Averages: [58.3 66.1 70.4 62.7 59.9]
Topper: Student 2 with 412 marks
Weakest: Student 5
Failed Students (indices): [3 7]
Grades: ['B' 'B' 'C' 'D' 'A' ...]
```

## 🧠 Key Learnings

- `axis=1` collapses across subjects → gives per-student results; `axis=0` collapses across students → gives per-subject results.
- `np.where(condition)` (single argument) returns the **indices** where a condition is true — useful for finding *which* students meet a criteria, not just how many.
- `np.where(condition, a, b)` can be **nested** to build multi-tier conditional logic (like a grading scale) without writing a loop or if-elif chain.
- Boolean masks (`student_avg < 40`) are the foundation for both filtering data and building `np.where` conditions.

## 📁 Files

- `student_analyzer.py` — main script

## ⏭️ Possible Extensions

- Add a "most improved subject" comparison
- Export results to a CSV using `np.savetxt`
- Visualize averages with a bar chart (matplotlib)

---

**Made by [Sudhanshu Dhande](https://github.com/sudhanshudhande19)**
