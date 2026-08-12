# Day 3 - Broadcasting

## 📌 Topics Covered
- Scalar broadcasting
- 1D array broadcasting across a 2D array
- Outer broadcasting (column + row vector)
- Broadcasting with `axis` in reduction operations
- `keepdims=True` and why it matters
- Incompatible shapes and broadcasting errors

## 💻 Problems Solved
1. Added a scalar to a 1D array — scalar applied to every element
2. Added a (3,) 1D array to a (3,3) 2D array — 1D array broadcast across every row
3. Added a (3,1) column array to a (1,3) row array — produced a (3,3) matrix (outer broadcasting)
4. Computed column-wise mean (`axis=0`) of a (4,3) matrix and subtracted it using broadcasting (normalization)
5. Tried adding incompatible shapes `(3,4)` and `(3,)` — observed the broadcasting error
6. **Challenge:** Normalized each row of a (5,5) matrix by its own row-max, no loops:
   ```python
   arr_max = np.max(arr, axis=1, keepdims=True)  # shape (5,1)
   kk = arr / arr_max
   ```

## 🧠 Key Learnings

**Broadcasting Rule (most important)**
> Compare shapes right-to-left. At each dimension: either equal, or one of them is 1. If both fail, error.

**`keepdims=True` — when to use it**
```python
arr.max(axis=1, keepdims=True)   # shape (n,1) — row-wise operations
arr.max(axis=0, keepdims=True)   # shape (1,n) — column-wise operations
```
Without `keepdims=True`, the reduced dimension is squeezed out entirely (e.g. `(5,5)` → `(5,)`), which NumPy then matches against the *last axis* by default — causing wrong-axis broadcasting instead of the intended row-wise/column-wise division.

**Row vs Column vector shapes**
- `(n,)` → ambiguous, matched against last axis (columns) by default
- `(n,1)` → column vector, broadcasts row-wise
- `(1,n)` → row vector, broadcasts column-wise

**Outer broadcasting**
`(3,1) + (1,3)` → `(3,3)` — both arrays expand in different directions.

**Real-world use cases**
- Normalization: `(arr - arr.mean(axis=1, keepdims=True)) / arr.std(axis=1, keepdims=True)`
- Softmax (deep learning): both the max-subtraction and sum-division steps need `keepdims=True`

## 📁 Files
- `day3_practice`

## ⏭️ Next
Day 4 — Axis Operations