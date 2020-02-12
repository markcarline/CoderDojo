# Write your code here :-)
from microbit import *
import neopixel
from math import floor

# Start calibrating
compass.calibrate()

num_pix = 23
neo = neopixel.NeoPixel(pin0, num_pix)

# get baseline field strength
baseline = compass.get_field_strength()
factor = 5
# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)

    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])

    # "15" is used for scaling
    npix = ( -1 * compass.heading()) // 15 % num_pix
    r = 0
    g = 255
    b = 0

    neo.clear()
    neo[npix] = (r, g, b)
    neo.show()
