# Day 7 - Linear Algebra Basics + Copy vs View

## 📌 Topics Covered
- Element-wise multiplication vs matrix multiplication
- `np.matmul()` / `@`
- Transpose (`.T`, `np.transpose()`)
- Determinant (`np.linalg.det()`)
- Inverse (`np.linalg.inv()`)
- Copy vs View (slicing vs `.copy()`)

## 💻 Problems Solved
1. Compared element-wise multiplication (`*`) vs matrix multiplication (`np.dot()`):
   ```python
   arr = np.array([[1,2],[3,4]])
   arr2 = np.array([[5,6],[7,8]])

   element_arr = arr * arr2        # [[5,12],[21,32]]
   matrix_arr = np.dot(arr, arr2)  # [[19,22],[43,50]]
   ```
2. Multiplied a (2,3) matrix with a (3,2) matrix using `np.matmul()` — checked resulting shape
3. Took the transpose of a (3,3) matrix and multiplied it with the original
4. Found the determinant of a (2,2) matrix using `np.linalg.det()`
5. Found the inverse of a (2,2) matrix using `np.linalg.inv()` and verified `matrix @ inverse ≈ identity`
6. **Copy vs View Challenge:** compared slicing (`a[1:4]`) vs `.copy()` and their effect on the original array

## 🧠 Key Learnings

**Element-wise vs Matrix multiplication**
- `*` → multiplies same-position elements directly, requires same shape, output is same shape
- `np.dot()` / `@` → real matrix multiplication (row · column dot products), requires columns of first matrix = rows of second matrix — this is the one used in linear algebra, ML, and transformations

**Slicing creates a view, not a copy**
> Slicing shares memory with the original array — modifying the slice modifies the original too.
> `.copy()` creates an independent array — modifying it leaves the original untouched.

This is a common source of bugs when data gets accidentally modified without realizing it.

## 📁 Files
- `day7_practice`

## ⏭️ Next
Day 8-9 — Real-world problems (end-to-end)