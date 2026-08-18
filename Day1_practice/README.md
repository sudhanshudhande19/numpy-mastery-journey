# Day 1 - NumPy Array Creation & Indexing

## 📌 Topics Covered
- Array creation (`np.array`, `np.zeros`, `np.ones`, `np.full`, `np.arange`, `np.linspace`)
- Array attributes (`.shape`, `.ndim`, `.size`, `.dtype`)
- Identity matrix (`np.eye`) & random matrix (`np.random.randint`)
- Pattern generation using indexing (chessboard challenge)

## 💻 Problems Solved
1. Created a 1D array (10 numbers) and a 2D array (3x3 matrix) using `np.array()`
2. Created 4x4 arrays using `np.zeros()`, `np.ones()`, and `np.full()` with different fill values
3. Compared `np.arange(0, 50, 5)` vs `np.linspace(0, 1, 10)`
4. Created a 5x5 array using `np.arange()` and checked `.shape`, `.ndim`, `.size`, `.dtype`
5. Created an identity matrix with `np.eye(4)` and a random 3x3 matrix with `np.random.randint()`
6. **Challenge:** Built a 6x6 chessboard pattern (alternating 0s and 1s) using indexing, no loops

## 🧠 Key Learnings
- `np.arange(start, stop, step)` takes a **step size**, while `np.linspace(start, stop, num)` takes the **number of points** to generate.
- `.shape` gives dimensions as a tuple, `.ndim` gives number of dimensions, `.size` gives total element count.
- Slicing with a step (e.g. `arr[::2] = 1`) is enough to build alternating patterns — no loop needed.

## 📁 Files
- `day1_practice`

## ⏭️ Next
Day 2 — Slicing, Boolean Indexing, Fancy Indexing
