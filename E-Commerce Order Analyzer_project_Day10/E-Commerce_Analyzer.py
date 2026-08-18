import numpy as np

np.random.seed(7)

products = ["Shirt", "Shoes", "Bag", "Watch", "Jacket", "Cap"]
prices = np.array([500, 1200, 800, 1500, 2000, 300])

orders = np.random.randint(0, 50, size=(30, 6))


# =========================================================
# 1. Find total revenue of each product for the whole month
# =========================================================

revenue = orders * prices

product_revenue = np.sum(revenue, axis=0)

print("1. Total Revenue of Each Product:")
for i in range(6):
    print(products[i], "=", product_revenue[i])


# =========================================================
# 2. Find total revenue of each day
# =========================================================

daily_revenue = np.sum(revenue, axis=1)

print("\n2. Total Revenue of Each Day:")
print(daily_revenue)


# =========================================================
# 3. Find best-selling product and highest revenue product
# =========================================================

total_units = np.sum(orders, axis=0)

best_selling_product = np.argmax(total_units)

highest_revenue_product = np.argmax(product_revenue)

print("\n3. Best Selling Product:")
print(products[best_selling_product])

print("Most Revenue Generating Product:")
print(products[highest_revenue_product])


# =========================================================
# 4. Find the day with the lowest sales
# =========================================================

worst_day = np.argmin(daily_revenue)

print("\n4. Day with Lowest Sales:")
print("Day", worst_day + 1)
print("Revenue =", daily_revenue[worst_day])


# =========================================================
# 5. Reshape data into weeks and find weekly revenue
# =========================================================

weekly_data = daily_revenue.reshape(5, 6)

weekly_revenue = np.sum(weekly_data, axis=1)

print("\n5. Weekly Revenue:")

for i in range(5):
    print("Week", i + 1, "=", weekly_revenue[i])


# =========================================================
# 6. Sort products according to total revenue
#    Highest to Lowest
# =========================================================

sorted_index = np.argsort(product_revenue)[::-1]

print("\n6. Products Sorted by Revenue:")

for i in sorted_index:
    print(products[i], "=", product_revenue[i])


# =========================================================
# 7. Normalize daily total revenue between 0 and 1
# =========================================================

normalized_revenue = (
    daily_revenue - np.min(daily_revenue)) / (np.max(daily_revenue) - np.min(daily_revenue))

print("\n7. Normalized Daily Revenue:")
print(normalized_revenue)


# =========================================================
# 8. Find days where revenue was above average
# =========================================================

average_revenue = np.mean(daily_revenue)

above_average = daily_revenue > average_revenue

print("\n8. Days with Revenue Above Average:")

for i in range(30):
    if above_average[i]:
        print("Day", i + 1, "=", daily_revenue[i])


# =========================================================
# 9. Standard deviation of daily sales for each product
# =========================================================

standard_deviation = np.std(orders, axis=0)

most_inconsistent = np.argmax(standard_deviation)

most_consistent = np.argmin(standard_deviation)

print("\n9. Standard Deviation of Each Product:")

for i in range(6):
    print(products[i], "=", standard_deviation[i])

print("Most Inconsistent Product =",products[most_inconsistent])

print("Most Consistent Product =",products[most_consistent])


# =========================================================
# 10. FINAL REPORT
# =========================================================

total_revenue = np.sum(daily_revenue)

best_week = np.argmax(weekly_revenue)

print("\n")
print("==========================================")
print("          E-COMMERCE SALES REPORT")
print("==========================================")

print("Total Revenue =", total_revenue)

print("Best Seller =",products[best_selling_product])

print("Most Profitable Product =",products[highest_revenue_product])

print("Most Consistent Product =",products[most_consistent])

print("Best Week = Week",best_week + 1)

print("Worst Day = Day",worst_day + 1)

print("==========================================")