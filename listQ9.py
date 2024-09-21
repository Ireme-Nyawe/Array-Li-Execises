# Program to create a list of product details and filter out products that are out of stock

products = [
    ["Rice", 1.00, 10],
    ["Beans", 0.50, 0],
    ["Flour", 2.00, 5],
    ["Potatoes", 3.00, 0],
    ["dodo",3.00,1]
]

available_products = [product for product in products if product[2] > 0]

print("Available products:")
for product in available_products:
    print(product)
