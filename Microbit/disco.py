# Write your code here :-)
from microbit import *
import neopixel
from random import randint


# Start calibrating
# compass.calibrate()

num_pix = 24
neo = neopixel.NeoPixel(pin0, num_pix)

sleep_amount = 200
skip_factor = 4

for i in range(num_pix/skip_factor):
    r, g, b = randint(0,255), randint(0,255), randint(0,255)
    neo[i*skip_factor] = (r,g,b)

neo.show()

while True:

    sleep(sleep_amount)

    for i in range(num_pix/skip_factor):
        r, g, b = neo[i*skip_factor]
        r, g, b = (r + randint(-10,10)) % 255, (g + randint(-10,10)) % 255, (b + randint(-10,10)) % 255
        neo[i*skip_factor] = (r,g,b)


    neo.show()