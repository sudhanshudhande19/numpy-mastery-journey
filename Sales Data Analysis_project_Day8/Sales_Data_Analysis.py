import numpy as np
np.random.seed(10)
sales = np.random.randint(50, 500, size=(30, 5))  # 30 days, 5 products

product_total_sales = np.sum(sales, axis=0)
print("Total Sale for each Product 30 Days =",product_total_sales)
print("---------------------------------")
each_day_total_sales = np.sum(sales,axis=1)
print("Total Sale Each Day 5 Product =",'\n',each_day_total_sales)
print("-------------------------------")
# 3
print("which Product Highest Overall Sales =",np.argmax(product_total_sales))
print("-------------------------------")
# 4
print("Which Day Lowest Sales =",np.argmin(each_day_total_sales))
print("-----------------------------")
# 5
product_find_day_400 = (np.unique(sales > 400)[0])
print("Finde Days more than 400 units product sold = ",'\n',product_find_day_400)
print("--------------------------")
# 6
reshape_data = sales.reshape((5,6,5))
print(reshape_data)
print("---------------------------")
# 7
first_week_avg = np.mean(sales[0:7])
last_week_avg = np.mean(sales[23:30])
print("First week average:", first_week_avg)
print("Last week average:", last_week_avg)
if last_week_avg > first_week_avg:
    print("Sales growth by", last_week_avg - first_week_avg)
else:
    print("Sales declined by", first_week_avg - last_week_avg)
print("---------------------------")
# 8
col_min = sales.min(axis=0, keepdims=True)   # shape (1,5)
col_max = sales.max(axis=0, keepdims=True)   # shape (1,5)

normalized = (sales - col_min) / (col_max - col_min)
print(normalized)
print("---------------------------")
# 9
print("Best performing Product =",'\n', np.argmax(product_total_sales))
print("worst Performing Day ="'\n',np.argmin(each_day_total_sales))
print("---------------------------")

prices = [10,15,8,20,12]
revenue_total = sales * prices
print("Total Revenue (overall):", np.sum(revenue_total))
print("Revenue per product:", np.sum(revenue_total, axis=0))