# MyMagicBall

import random

# put answers in a 'list' 

answers = [
    "Go for it!",
    "No way Jose!",
    "I'm not sure, ask me again..",
    "Fear of the unknown is what imprisons us...",
    "It would be utter madness to do that!!",
    "Only you can save mankind :-)",
    "Don't care, do whatever you want..",
    "Yes, Yes, Yes!!!!"
    ]

# get users name
name = input("What is your name? ")
print("\nHi", name)

#get users input
question = input("Ask for advice then press ENTER to shake me (A Yes/No question).\n")
print("Shaking ....\n" * 4)

# use the randit() function to select answer
choice = random.randint(0, 7)
print(answers[choice], "choice was", choice)

# Exit nicely
print("Thank you for playing", name, "- hope this helped")
input("\n\nPress the ENTER key to finish!")
