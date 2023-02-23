import random

value = 0
while value < 1:

    # Initialize the throw count and the dice values
    throw_count = 0
    dice1 = 0
    dice2 = 0

    # Keep rolling the dice until they match
    while dice1 != dice2:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        throw_count += 1
        print("Throw", throw_count, ":", dice1, dice2)

    # Print the result
    print("Matching pair found after", throw_count, "throws:", dice1, dice2)
