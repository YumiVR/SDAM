# Import the sys module
import sys

# Welcome message
print("Welcome to the program")
print("Press enter to exit the program")

# Dictionary of song verses
song = {
    1: "One for Sorrow",
    2: "Two for Joy",
    3: "Three for a Girl",
    4: "Four for a Boy",
    5: "Five for Silver",
    6: "Six for Gold",
    7: "Seven for a secret never to be told"
}

# Infinite loop to keep the program running until user decides to exit
while True:
    try:
        # Prompt user for a number
        number = int(input("Enter a number: "))

        # Print the corresponding verse from the song dictionary
        print(song[number])

    except:
        # If the user enters an invalid number, print an error message
        print("Not a permitted number")
        print("Would you like to exit?")

        # Prompt user for input to exit or continue
        user_input = input("(y) for Yes or (n) for No > ")

        # Check user input and exit the program if user wants to
        if user_input == 'y':
            sys.exit()
        elif user_input == 'n':
            print("No Exit")
