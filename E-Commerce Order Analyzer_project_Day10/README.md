# 📅 Day 10 — Capstone Project: E-Commerce Order Analyzer

## 📌 Project Overview

This project is a **NumPy-based E-Commerce Order Analyzer**.

It analyzes **30 days of sales data** for 6 different products and calculates product-wise revenue, daily revenue, weekly revenue, best-selling products, sales consistency, and other useful business insights.

## 🛠️ Technologies Used

* Python
* NumPy

## 🛍️ Products & Prices

| Product | Price |
| ------- | ----: |
| Shirt   |  ₹500 |
| Shoes   | ₹1200 |
| Bag     |  ₹800 |
| Watch   | ₹1500 |
| Jacket  | ₹2000 |
| Cap     |  ₹300 |

## 📊 Dataset

```python
np.random.seed(7)

orders = np.random.randint(0, 50, size=(30, 6))
```

* **30 rows** = 30 days
* **6 columns** = 6 products
* Values represent **units sold per day**

## 🎯 Project Questions

1. Find the total revenue of each product for the whole month.
2. Find the total revenue of each day.
3. Find the best-selling product and the highest-revenue product.
4. Find the day with the lowest sales.
5. Reshape the data into 5 weeks and calculate weekly revenue.
6. Sort products according to their total revenue from highest to lowest.
7. Normalize daily revenue between 0 and 1.
8. Find days where total revenue was above the average.
9. Calculate the standard deviation of daily sales and find the most inconsistent and most consistent product.
10. Generate a final sales report containing:

* Total Revenue
* Best Seller
* Most Profitable Product
* Most Consistent Product
* Best Week
* Worst Day

## 🧠 NumPy Concepts Used

* NumPy Arrays
* `np.sum()`
* `np.mean()`
* `np.min()`
* `np.max()`
* `np.argmax()`
* `np.argmin()`
* `np.argsort()`
* `np.std()`
* `reshape()`
* Boolean Filtering
* Min-Max Normalization
* `axis=0`
* `axis=1`
* Array Multiplication

## 🔑 Important Logic

Revenue is calculated using:

```python
revenue = orders * prices
```

Product-wise revenue:

```python
product_revenue = np.sum(revenue, axis=0)
```

Daily revenue:

```python
daily_revenue = np.sum(revenue, axis=1)
```

Weekly revenue:

```python
weekly_data = daily_revenue.reshape(5, 6)
weekly_revenue = np.sum(weekly_data, axis=1)
```

## 📂 Project Structure

```text
Day10/
│
├── ecommerce_order_analyzer.py
└── README.md
```

## ▶️ How to Run

Install NumPy:

```bash
pip install numpy
```

Run the Python file:

```bash
python ecommerce_order_analyzer.py
```

## 📈 Learning Outcome

After completing this project, you will have practical experience with:

* 2D NumPy arrays
* Array operations
* Aggregation functions
* `axis=0` and `axis=1`
* Reshaping data
* Sorting data
* Statistical analysis
* Standard deviation
* Data normalization
* Boolean filtering
* Real-world sales data analysis

## 👨‍💻 Project

**Day 10 — E-Commerce Order Analyzer**

Built as part of **Python & NumPy practice**.
