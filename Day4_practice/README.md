# Day 4 - Axis Operations

## 📌 Topics Covered
- `sum`, `mean`, `max`, `min` with `axis=0` and `axis=1`
- `argmax` and `argmin` along an axis
- `keepdims=True` in reduction operations
- Verifying totals across axes

## 💻 Problems Solved
1. Found `sum(axis=0)` and `sum(axis=1)` on a (4,4) matrix — compared row-wise vs column-wise sums
2. Found `mean(axis=0)` and `mean(axis=1)` — column averages vs row averages
3. Tried `max()` and `min()` with both axes — noted result shapes
4. Used `argmax()` and `argmin()` to find the index of the largest/smallest value in each row
5. Verified that column-wise total sum (`axis=0`) equals row-wise total sum (`axis=1`) on a (5,3) matrix
6. **Challenge:** Student marks matrix (3 students, 4 subjects):
   ```python
   stu_total = np.sum(arr, axis=1, keepdims=True)
   stu_total_avg = stu_total / arr.shape[1]   # divide by number of subjects

   sub_total = np.sum(arr, axis=0, keepdims=True)
   sub_total_avg = sub_total / arr.shape[0]   # divide by number of students

   top_student = np.argmax(stu_total)
   ```

## 🧠 Key Learnings
- `axis=0` operates **through the columns** — collapses top to bottom, result has one row's worth of output.
- `axis=1` operates **through the rows** — collapses left to right, result has one column's worth of output.
- Quick rule: the axis number is the dimension that **disappears** in the result.
- `len(arr)` only gives the size of the **first dimension**, not the total count needed for an average — use `arr.shape[i]` for the correct dimension size instead.
- `argmax(axis=1)` on an array that already has only one value per row (shape `(n,1)`) is meaningless — it will always return `0`. To compare *across* rows, use `argmax` on the flattened array or `axis=0`.

## 📁 Files
- `day4_practice`

## ⏭️ Next
Day 5 — (topic TBD)