# Program to store and display weekly sales of different products in a 2D array (products x days)

products = []

num_products = int(input("Enter the number of products: "))
for i in range(num_products):
    product_name = input(f"\nEnter the name of Product {i + 1}: ")
    daily_sales = []
    
    print(f"Enter sales for {product_name}:")
    for j in range(7):
        sale = float(input(f"Day {j + 1} sales: "))
        daily_sales.append(sale)
    
    products.append([product_name, daily_sales])

print("\nWeekly sales of products:")
for product in products:
    print(f"{product[0]}: {product[1]}")
