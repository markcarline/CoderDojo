#Import module used for pibrella access
import pibrella

#import module used for GPIO access
import RPi.GPIO as GPIO

#import time module: for time delay
import time

#import random mudule to generate random number
import random

# Setup some constants used for GPIO LEDs (these same same as Pibrella)
#  RED    = BCM Port 27 = Pin 13
#  YELLOW = BCM Port 17 = Pin 11
#  GREEN  = BCM Port  4 = Pin  7
LED_RED=27

# Setup the GPIO ports:
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)

# Subroutine to flash red:
def flash_red(t):
    GPIO.output(LED_RED, True)
    time.sleep(t)
    GPIO.output(LED_RED, False)
    time.sleep(t)
    

count = random.randint(1,10)


print ("Hi, The LED will flash "+ str(count) + " times")

loop = 1
while loop <= count:
    flash_red(0.5)
    loop+=1

pibrella.buzzer.success()
