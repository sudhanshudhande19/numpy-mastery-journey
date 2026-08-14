# Day 5 - Reshaping & Stacking

## 📌 Topics Covered
- Reshaping arrays (`reshape`) into 2D and 3D shapes
- Flattening arrays (`flatten` vs `ravel`)
- Transposing arrays (`transpose` / `.T`)
- Combining arrays (`vstack`, `hstack`, `concatenate`)

## 💻 Problems Solved
1. Reshaped a 12-element 1D array into (3,4) and (4,3) shapes
2. Reshaped the same array into a 3D shape (2,2,3)
3. Converted a 2D array to 1D using both `.flatten()` and `.ravel()`
4. Transposed a (3,4) matrix into (4,3) using `.transpose()` / `.T`
5. Combined two (2,3) arrays vertically (`vstack`) and horizontally (`hstack`)
6. **Challenge:** Combined three (2,2) arrays using `np.concatenate()` along `axis=0` and `axis=1`

## 🧠 Key Learnings
- `reshape()` requires the total number of elements to stay the same — a (12,) array can become (3,4) since 3×4=12, but not (3,5) since 3×5≠12.
- `flatten()` always returns a **new copy** — modifying the flattened array does not affect the original.
- `ravel()` returns a **view** of the original when possible — modifying the raveled array can change the original.
- `transpose()` / `.T` swaps rows and columns — a (3,4) matrix becomes (4,3).
- `vstack()` = `concatenate(axis=0)`, `hstack()` = `concatenate(axis=1)` — stacking functions are shortcuts for `concatenate` along a fixed axis.

## 📁 Files
- `day5_practice.py`

## ⏭️ Next
Day 6 — Statistics & Sorting/Searching