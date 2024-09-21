# Python program to store and print temperature readings for 7 days

temperature_readings=[]
print("Enter temperature readings for 7 days:")
for i in range(7):
    temperature_readings.append(float(input(f"Day {i+1}(°C): ")))

print("\nTemperature readings for 7 days:")
for i in range(7):
    print(f"Day {i+1}: {temperature_readings[i]}°C")
