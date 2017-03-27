# Craps dictionary

import random


def rollDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('You have rolled a', dice1, 'and', dice2)
    roll_of_dice = dice1+dice2
    return roll_of_dice

roll_dice = rollDice()

print('So total dice roll is', roll_dice)


poss_roll = {
    2:'lose',
    3:'lose',
    4:'point',
    5:'point',
    6:'point',
    7:'win',
    8:'point',
    9:'point',
    10:'point',
    11:'win',
    12:'lose',
    }

returnval = poss_roll[roll_dice]

print('Thats a', returnval)

# If we are at this stage, we have rolled a point score
while returnval == "point":
    print('\nYou must roll a', roll_dice, 'before a 7 to win')
    input('Press ENTER to continue')
    pointvalue = roll_dice
    roll_dice2 = rollDice()
    print(roll_dice2)
    if roll_dice2 == 7:
        returnval = 'lose'
    else:
        if roll_dice2 == pointvalue:
            returnval = 'win'


if returnval == "win":
    print('\nFANTASTIC!! You are the winner')

if returnval == "lose":
    print('\nOhhhh, you are such a LOSER')






    

