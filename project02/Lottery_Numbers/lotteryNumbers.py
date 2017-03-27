# lottery Numbers in Python

import random

# generate list of all balls
balls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
         27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]

# shuffle balls
random.shuffle(balls)

# print("Lottery Numbers:", balls[0],
#      balls[1],balls[2],balls[3],balls[4], "Bonus ball:", balls[5])

print("Lottery Numbers:", balls[0:5], "Bonus ball:", balls[5])
