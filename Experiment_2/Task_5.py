import matplotlib.pyplot as plt

sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]
total_sales = 0
for s in sales_data:
    total_sales += s
average_sales = total_sales / len(sales_data)
max_value = sales_data[0]
max_month = 1
for i in range(len(sales_data)):
    if sales_data[i] > max_value:
        max_value = sales_data[i]
        max_month = i + 1
plt.figure()
plt.plot(range(1, 13), sales_data, marker='o')
plt.scatter([max_month], [max_value])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.annotate("Highest", (max_month, max_value))
plt.show()
print("Total sales:", total_sales)
print("Average sales:", round(average_sales,2))
print("Month with highest sales:", max_month)