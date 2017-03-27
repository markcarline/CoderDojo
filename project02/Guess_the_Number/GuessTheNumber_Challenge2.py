# GuessTheNumber.py
# This game uses a home made function

import random

name = input('What is your name? ')
print ('\nHello', name)

# What level shall we play - Easy, Medium, or hard
selection = input("What level shall we play?\nSelect either e\\m\\h <ENTER> for easy, medium, or hard: ")

# Find a way of making sure Players only type e, m, or h
while selection != "e" and selection != "m" and selection != "h":
    selection = input("Sorry. You must type in one of the letters 'e', 'm', or 'h'\ne/m/h: ")
    
# figure out what the upper limit needs to be
upper_limit = 0
if selection == "e":
    upper_limit = 20
elif selection == "m":
    upper_limit = 50
else:
    upper_limit = 100 
                

# Computer thinks of a number
computer_number = random.randint(1, upper_limit)

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
print ("\nI have now thought of a number netween 1 and", upper_limit)

# How many guesses does it take - We will keep a note as the
# game continues using this variable
counter = 0

# Get the Players to guess (as an integer)
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
