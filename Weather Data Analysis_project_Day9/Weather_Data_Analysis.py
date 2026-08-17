print("========Weather Data Analysis==========")

import numpy as np

cities = ["Nagpur", "Delhi", "Mumbai", "Shimla"]
# Rows = cities, Columns = months (Jan to Dec)
temp = np.array([
    [20, 24, 30, 35, 40, 38, 33, 32, 31, 28, 24, 21],  # Nagpur
    [15, 18, 25, 32, 38, 40, 35, 33, 32, 28, 20, 16],  # Delhi
    [24, 25, 28, 30, 32, 30, 28, 27, 28, 29, 27, 25],  # Mumbai
    [5, 8, 12, 18, 55, 24, 22, 20, 18, 14, 9, 0]       # Shimla
])

# 1 Find each city's yearly average temperature
city_year_avg_temp = np.mean(temp,axis=1)
print("each city's yearly average temperature =",city_year_avg_temp)

print("-----------------------------------------------")
# 2 find the average temperature across all cities for each month and figure out which month is overall the hottest.
month_avg_temp =np.mean(temp,axis=0)
print(f"average temperature across all cities for each months = \n{month_avg_temp}\nOverall the hottest. months is = {np.argmax(month_avg_temp)}")
print("-----------------------------------------------")

# 3Find each city's hottest and coldest month
for i in range(len(cities)):
    print(f"{cities[i]} hottest month = {np.argmax(temp[i])}, coldest month = {np.argmin(temp[i])}")
print("-----------------------------------------------")

# 4 Find the city with the most temperature variation — this needs standard deviation
temperature_variation  = np.std(temp,axis=1)
print("Hight Variation Citys is =",np.argmax(temperature_variation))
print("-----------------------------------------------")

# 5 Use boolean masking to find which (city, month) combinations went above 35°C.
hot_mask = temp > 35
print("Hot combinations (True=hot):\n", hot_mask)

# Actual (city, month) pairs 
city_idx, month_idx = np.where(temp > 35)
for c, m in zip(city_idx, month_idx):
    print(f"{cities[c]} in month {m+1} — {temp[c][m]}°C")
print("-----------------------------------------------")

# 6 sort the cities by their yearly average temperature (coldest to hottest order).
print("coldest to hottest order Citys = ",np.argsort(city_year_avg_temp))
print("-----------------------------------------------")

# 7 Temperature Anomaly Detector: For each city, find how much each month deviates from that city's own average
city_year_avg_temp = np.mean(temp, axis=1, keepdims=True)   # shape (4,1)
temperature_variation = np.std(temp, axis=1, keepdims=True)  # shape (4,1)

normal_avg = (temp - city_year_avg_temp) / temperature_variation
print(normal_avg)