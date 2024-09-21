# Program to store daily temperature readings of cities for a week and calculate average temperature

temperatures = []
city_names = []

num_cities = 4
num_days = 7

for i in range(num_cities):
    city_name = input(f"Enter the name of City {i + 1}: ")
    city_names.append(city_name)
    city_temperatures = []
    print(f"Enter temperatures for {city_name}:")
    for j in range(num_days):
        temp = float(input(f"Day {j + 1} temperature: "))
        city_temperatures.append(temp)
    temperatures.append(city_temperatures)

print("\nAverage temperatures for each city:")
for i in range(num_cities):
    average_temp = sum(temperatures[i]) / num_days
    print(f"{city_names[i]}: Average Temperature = {average_temp:.2f}")
