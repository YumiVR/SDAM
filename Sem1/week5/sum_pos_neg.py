# Initialize the sum of positive and negative integers
sum_positive = 0
sum_negative = 0

# Prompt the user to enter 10 integer values
for i in range(10):
    num = int(input("Enter an integer: "))
    if num > 0:
        sum_positive += num
    else:
        sum_negative += num

# Print the sum of positive and negative integers
print("Sum of positive integers:", sum_positive)
print("Sum of negative integers:", sum_negative)
