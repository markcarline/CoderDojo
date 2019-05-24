from microbit import *
import neopixel
import random

num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix) # create a NeoPixel object on pin0

p = 0 # set pixel pointer to 0
while True:
    #Set Random RGB Values
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    p = random.randint(0,23) # random LED
    
    np.clear()
    np[p] = (60,0,0) # set the RGB values to be blue (red=0, green=0, blue=60)
    np.show()
    sleep(5)
