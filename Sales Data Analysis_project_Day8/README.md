# Day 8 - Real-World Problem: Sales Data Analysis

## 📌 Topics Covered
- Combining everything from Day 1-7 into one real-world scenario
- Axis operations (`sum`, `argmax`, `argmin`) on a realistic dataset
- Boolean masking with `np.where()` to find matching indices
- `np.unique()` to remove duplicate indices
- Reshaping data into a meaningful multi-dimensional structure
- Broadcasting for normalization and revenue calculation

## 💻 Problem Solved
Analyzed 30 days of sales data across 5 products (`(30,5)` array):

1. Found each product's total sales across all 30 days (`axis=0`)
2. Found each day's total sales across all 5 products (`axis=1`)
3. Found the best-selling product using `argmax`
4. Found the lowest-sales day using `argmin`
5. Found the days where any product sold more than 400 units:
   ```python
   days_with_high_sales = np.unique(np.where(sales > 400)[0])
   ```
6. Reshaped `(30,5)` into `(5,6,5)` — representing 5 weeks of 6-day blocks
7. Compared first week vs last week averages:
   ```python
   first_week_avg = np.mean(sales[0:7])
   last_week_avg = np.mean(sales[23:30])
   ```
8. Normalized each product's sales to a 0-1 range using min-max scaling:
   ```python
   col_min = sales.min(axis=0, keepdims=True)
   col_max = sales.max(axis=0, keepdims=True)
   normalized = (sales - col_min) / (col_max - col_min)
   ```
9. Built a sales report: best product, worst day, and total revenue using price broadcasting:
   ```python
   prices = [10, 15, 8, 20, 12]
   revenue_total = sales * prices
   ```

## 🧠 Key Learnings
- `np.where(condition)` without slicing `[0]` returns indices for **every matching cell** (both row and column) — if a question asks for matching *rows* (like "which days"), extract `[0]` and pass through `np.unique()` to remove duplicate day numbers when multiple products match on the same day.
- `sum` and `mean` answer different questions — sum gives total volume, mean gives average performance per day. When comparing periods of data (e.g. week 1 vs week 4), `mean` is the fairer comparison since it isn't affected by the number of days.
- Reshaping `(30,5)` → `(5,6,5)` works because NumPy fills data in row-major order — so each block of 6 consecutive days becomes one "week" automatically.
- Broadcasting a 1D price list `(5,)` against a `(30,5)` sales array works because NumPy aligns `(5,)` with the last dimension (columns) automatically — no `keepdims` needed here since we're not reducing, just multiplying element-wise per column.

## 📁 Files
- `day8_practice`

## ⏭️ Next
Day 9 — (Statistics / Sorting — carried over from earlier plan)