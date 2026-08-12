# Day 2 - Slicing, Boolean & Fancy Indexing

## 📌 Topics Covered
- Slicing 1D and 2D arrays
- Boolean masking (`arr[condition]`)
- Combined boolean conditions using `&`
- Fancy indexing with index lists

## 💻 Problems Solved
1. Sliced a 10-element array to get only even-index elements
2. Extracted a specific row and column from a 5x5 2D array using slicing
   - `arr[3]` → row at index 3
   - `arr[:, 3]` → column at index 3 (all rows, 4th column)
3. Extracted all numbers greater than 50 from an array using boolean indexing
4. Extracted elements at specific indices (e.g. `[1, 3, 5]`) using fancy indexing
5. Replaced all negative numbers in a 2D array with 0 using boolean masking:
   ```python
   arr[arr < 0] = 0
   ```
6. **Challenge:** Extracted elements divisible by both 3 AND 5 using a combined boolean condition:
   ```python
   mask = (arr % 3 == 0) & (arr % 5 == 0)
   print(arr[mask])
   ```
   Output: `[15 30 30 15]`

## 🧠 Key Learnings
- `arr[:] = 0` overwrites the **entire array**, regardless of condition — not the same as boolean masking. Masking must use a condition like `arr[arr < 0] = 0`.
- For combined conditions on NumPy arrays, use `&` (not Python's `and`), and wrap each condition in parentheses: `(cond1) & (cond2)` — otherwise operator precedence causes errors.
- `arr[row_index]` gives a row; `arr[:, col_index]` gives a column — the `:` means "all rows."

## 📁 Files
- `day2_practice`

## ⏭️ Next
Day 3 — Broadcasting