# Import time module - Used for delay
import time

# Import module used for GPIO access
import RPi.GPIO as GPIO

# Setup some constants used for GPIO LEDs (these same same as Pibrella)
#  RED    = BCM Port 27 = Pin 13
#  YELLOW = BCM Port 17 = Pin 11
#  GREEN  = BCM Port  4 = Pin  7
LED_RED=27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)

def flash(t):
    GPIO.output(LED_RED, True)
    time.sleep(t)
    GPIO.output(LED_RED, False)
    time.sleep(t)

try:
    while True:
        flash(0.5)
finally:
    GPIO.cleanup()
