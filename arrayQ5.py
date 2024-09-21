# Program to count the number of even and odd numbers in a list of random numbers

numbers = []

num_elements = int(input("Enter(specify) the number of elements to be in the list: "))
print("Enter the numbers:")

for i in range(num_elements):
    numbers.append(int(input(f"Number {i+1}: ")))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"\nNumber of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
