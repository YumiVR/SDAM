# Importing sys module for future use, if required
import sys

# Initializing valid flag as False
valid = False

# Loop until a valid input is received from the user
while not valid:
    try:
        # Initializing sum of positive and negative numbers to zero
        sumpos = 0
        sumneg = 0

        # Prompting the user for input of 5 numbers
        usernum1 = int(input("Enter First Number: "))
        usernum2 = int(input("Enter Second Number: "))
        usernum3 = int(input("Enter Third Number: "))
        usernum4 = int(input("Enter Fourth Number: "))
        usernum5 = int(input("Enter Fifth Number: "))

        # Setting valid flag as True
        valid = True

    except:
        # If an exception occurs, invalid input was received
        print ("Invalid input, Try Again Please! ")

# Checking if the first number is negative, if yes, add to sum of negative numbers
if usernum1 < 0:
    sumneg = sumneg + usernum1
else:
    # If the first number is positive, add to sum of positive numbers
    sumpos	= sumpos + usernum1

# Checking if the second number is negative, if yes, add to sum of negative numbers
if usernum2 < 0:
    sumneg = sumneg + usernum2
else:
    # If the second number is positive, add to sum of positive numbers
    sumpos = sumpos + usernum2

# Checking if the third number is negative, if yes, add to sum of negative numbers
if usernum3 < 0:
    sumneg = sumneg + usernum3
else:
    # If the third number is positive, add to sum of positive numbers
    sumpos = sumpos + usernum3

# Checking if the fourth number is negative, if yes, add to sum of negative numbers
if usernum4 < 0:
    sumneg = sumneg + usernum4
else:
    # If the fourth number is positive, add to sum of positive numbers
    sumpos = sumpos + usernum4

# Checking if the fifth number is negative, if yes, add to sum of negative numbers
if usernum5 < 0:
    sumneg = sumneg + usernum5
else:
    # If the fifth number is positive, add to sum of positive numbers
    sumpos = sumpos + usernum5

# Printing the sum of negative and positive numbers
print ("Sum of Negative Intergers >", sumneg)
print ("Sum of Positive Intergers >", sumpos)
