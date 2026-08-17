# Day 9 - Real-World Problem: Weather Data Analysis

## 📌 Topics Covered
- Combining axis operations, argmax/argmin, boolean masking, broadcasting on a real dataset
- `np.std()` for measuring variation/spread
- `np.argsort()` for getting sorted-order indices
- `np.where()` on a 2D array to get (row, column) index pairs
- Correct use of `keepdims=True` when combining a reduced result with the original array

## 💻 Problems Solved
1. Found each city's yearly average temperature (`axis=1`)
2. Found the average temperature across all cities for each month (`axis=0`) and identified the hottest month
3. Found each city's hottest and coldest month using `argmax`/`argmin` per row
4. Found the city with the most temperature variation using `np.std(axis=1)`
5. Found which (city, month) combinations went above 35°C using boolean masking + `np.where()`
6. Sorted cities from coldest to hottest yearly average using `np.argsort()`
7. **Challenge:** Built a temperature anomaly detector — how much each month deviates from a city's own average:
   ```python
   city_year_avg_temp = np.mean(temp, axis=1, keepdims=True)     # shape (4,1)
   temperature_variation = np.std(temp, axis=1, keepdims=True)   # shape (4,1)
   normal_avg = (temp - city_year_avg_temp) / temperature_variation
   ```

## 🧠 Key Learnings / Mistakes Fixed

- **`argmax`/`argmin` return an index, not a value.** Comparing `np.argmax(arr) > 35` compares an *index* to 35, not an actual temperature — a common but serious logic bug.
- **To find which (row, col) pairs satisfy a condition in a 2D array**, use `np.where(condition)` — it returns two arrays: row indices and column indices. Zip them together to get the actual pairs:
  ```python
  city_idx, month_idx = np.where(temp > 35)
  ```
- **`keepdims=True` is essential whenever a reduced (1D) result needs to be combined with the original 2D array.** Without it, shapes like `(4,)` and `(4,12)` don't align during broadcasting (right-to-left comparison fails), causing an error or silently wrong results. Using `axis=1, keepdims=True` gives shape `(4,1)`, which broadcasts correctly row-wise.
- **Avoid repeating the same line 4 times for 4 cities** — either loop over `range(len(cities))`, or better, use the axis-based version (`np.argmax(temp, axis=1)`) to get all cities' answers in one call.
- `np.std()` measures how spread out values are — higher std means more fluctuation/variation in the data.
- `np.argsort()` returns the **indices** that would sort the array, not the sorted values themselves.

## 📁 Files
- `day9_weather_analysis.py`

## ⏭️ Next
Day 10 — Combine everything into a bigger project