# GuessTheNumber.py
# This game uses a home made function

import random

# Computer thinks of a number
computer_number = random.randint(1, 50)

# How many guesses does it take
counter = 0

# Create the function does_it_match()
def does_it_match(target, number):
    if target == number:
        result = "Win"
    elif target > number:
        result = "Low"
    else:
        result = "High"
    return result

# Lets Start the Game
name = input('What is your name? ')
print ('\nHello', name, 'I have now thought of a number netween 1 and 50!')

# Get the Players guess (as an integer)
guess = int(input("Try and guess the number I'm thinking of.. "))
counter = counter + 1

# Now lets use our newly created function (does_it_match() )
higher_or_lower = does_it_match(computer_number, guess)

# Lets keep going until the Player guesses the number
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("Ooops, too low, try again!! "))
        counter = counter + 1
    else:
        guess = int(input("Ohh no, too high, have another go!! "))
        counter = counter + 1

    higher_or_lower = does_it_match(computer_number, guess)

# If they match, lets end the game
print("\nFANTASTIC, you guessed it, it took", counter, "guesses!")
input("\nWELL DONE!!\n\n\nPress ENTER to exit!")
