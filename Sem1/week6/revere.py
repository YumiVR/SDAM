# Prompt the user for 5 integers
numbers = []
for i in range(5):
    number = int(input(f"Enter integer {i + 1}: "))
    numbers.append(number)

# Reverse and print the inputted integers
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
