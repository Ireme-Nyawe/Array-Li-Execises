# program to Store and calculate the average of daily sales of a shop over a week.

sales = []
print("Enter the daily sales for 7 days (Week):")
for i in range(7):
    sales.append(float(input(f"Sales for Day {i+1}: ")))

total_sales = sum(sales)
average_sales = round(total_sales / 7, 2)
print(f"\nWhole week sales: {total_sales}")
print(f"Average daily sales: {average_sales}")
