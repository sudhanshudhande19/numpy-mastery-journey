# Day 6 - Statistics + Sorting/Searching

## 📌 Topics Covered
- Statistical functions (`mean`, `median`, `std`, `var`)
- Axis-wise statistics
- Cumulative functions (`cumsum`, `cumprod`)
- Sorting (`sort`, `argsort`)
- `unique()` for removing duplicates
- `where()` for conditional index search

## 💻 Problems Solved
1. Found `mean`, `median`, `std`, `var` of an array and verified `std = sqrt(var)`
2. Compared `std(axis=0)` vs `std(axis=1)` on a (4,4) matrix
3. Used `cumsum()` and `cumprod()` on a 1D array to understand running totals
4. **Real use case:** Calculated cumulative daily sales using `cumsum()`
5. Sorted an array with `sort()` and found sorting indices with `argsort()`
6. Removed duplicates from an array using `unique()`
7. Found indices where values exceed a threshold using `where()`
8. **Challenge:** Exam scores analysis —
   - Top 3 scores using `sort()`
   - Original indices of top 3 scores using `argsort()`
   - Number of failing students (score < 40) using `where()`

## 🧠 Key Learnings
- `sort()` returns the **sorted values**, `argsort()` returns the **indices** needed to sort the array. Use `argsort()` when you need to trace a value back to its original position (e.g. "which student scored this").
- `std = sqrt(var)` — standard deviation is just the square root of variance; both measure spread, but `std` is in the same unit as the data.
- `cumsum()` builds a running total (each element = sum of all elements up to that point); `cumprod()` does the same with multiplication.
- `axis=0` vs `axis=1` applies to statistical functions too, not just `sum`/`mean` — same collapse rule: `axis=0` collapses rows, `axis=1` collapses columns.

## 📁 Files
- `day6_practice`

## ⏭️ Next
Day 7 — Linear Algebra Basics + Copy vs View