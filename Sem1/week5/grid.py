# Prompt user for the number of columns
width = int(input("Enter the number of columns: "))

# Prompt user for the number of rows
height = int(input("Enter the number of rows: "))

# Nested loop to print the grid of asterisks
for i in range(height):
    for j in range(width):
        print("*", end="")
    print("")
