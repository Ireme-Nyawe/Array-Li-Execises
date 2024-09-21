# Program to find the maximum and minimum stock prices in a week

stock_prices = []

print("Enter the daily stock prices for 7 days:")
for i in range(7):
    stock_prices.append(float(input(f"Stock price for Day {i+1}: ")))

max_price = max(stock_prices)
min_price = min(stock_prices)

print(f"\nMaximum stock price for the week: {max_price}")
print(f"Minimum stock price for the week: {min_price}")
