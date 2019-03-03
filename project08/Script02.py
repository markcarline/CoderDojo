# GuessTheNumber.py
# This game uses a home made function

import random
import pibrella
import time
import RPi.GPIO as GPIO


# Computer thinks of a number
computer_number = random.randint(1, 50)

# How many guesses does it take
counter = 0

# Setup some constants used for GPIO LEDs (these same same as Pibrella)
#  RED    = BCM Port 27 = Pin 13
#  YELLOW = BCM Port 17 = Pin 11
#  GREEN  = BCM Port  4 = Pin  7
LED_RED=27
#LED_YELLOW=17
#LED_GREEN=4

# Setup the GPIO ports:
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
#GPIO.setup(LED_YELLOW, GPIO.OUT)
#GPIO.setup(LED_GREEN, GPIO.OUT)


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
name = raw_input('What is your name? ')
print ("\nHello " + name + " I have now thought of a number netween 1 and 50!")

# Get the Players guess (as an integer)
guess = int(raw_input("Try and guess the number I'm thinking of: "))
counter = counter + 1

# Now lets use our newly created function (does_it_match() )
higher_or_lower = does_it_match(computer_number, guess)

# Lets keep going until the Player guesses the number
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        GPIO.output(LED_RED,True)
        time.sleep(1)
        GPIO.output(LED_RED,False)
        guess = int(raw_input("Ooops, too low, try again!! "))
        #pibrella.buzzer.fail()
        
        counter = counter + 1
        
    else:
        GPIO.output(LED_RED,True)
        time.sleep(1)
        GPIO.output(LED_RED,False)
        guess = int(raw_input("Ohh no, too high, have another go!! "))
        #pibrella.buzzer.fail()
        
        counter = counter + 1

    higher_or_lower = does_it_match(computer_number, guess)

# If they match, lets end the game
print("\nFANTASTIC, you guessed it, it took", counter, "guesses!")
pibrella.buzzer.success()
raw_input("\nWELL DONE!!\n\n\nPress ENTER to exit!")

