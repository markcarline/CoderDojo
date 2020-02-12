# Write your code here :-)
from microbit import *
import neopixel
from math import e


# Start calibrating
# compass.calibrate()

num_pix = 24
neo = neopixel.NeoPixel(pin0, num_pix)

def tanh(x):
    return (e**(2*x)-1)/(e**(2*x)+1)

def scaleSleep(x, factor, y=250):
    return  y * (-0.5*tanh(x/factor - 1) + 1)

# get baseline field strength
baseline = compass.get_field_strength()
factor = 200000
# Try to keep the needle pointed in (roughly) the correct direction
while True:
    neo.clear()

    sleep_ammount = scaleSleep(compass.get_field_strength(), factor)
    sleep(sleep_ammount)
    # needle = ((15 - compass.heading()) // 30) % 12
    # display.show(Image.ALL_CLOCKS[needle])

    # npix = (-1 * compass.heading()) // 15 % num_pix
    r = 0
    g = 255
    b = 0

    for i in range(num_pix):
        neo[i] = (r, g, b)

    neo.show()
    sleep(sleep_ammount)