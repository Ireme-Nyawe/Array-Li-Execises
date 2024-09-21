# Program to store monthly expenses and calculate the average per category

expenses = [
    [1200, 300, 150],
    [1300, 250, 180],
    [1250, 320, 160],
    [1400, 280, 200],
    [1350, 300, 170],
    [1280, 310, 190]
]

averages = [sum(x) / len(x) for x in zip(*expenses)]
categories = ["Rent", "Food", "Utilities"]

print("Average monthly expenses per category($):")
for category, average in zip(categories, averages):
    print(f"{category}: ${average:.2f}")
