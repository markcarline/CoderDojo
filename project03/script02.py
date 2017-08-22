# Import time module - Used for delay
import time

# Import module used for GPIO access
import RPi.GPIO as GPIO

# Import minecraft modules
import mcpi.minecraft as minecraft
import mcpi.block as block
# and connect to world
mc = minecraft.Minecraft.create()

# Setup some constants used for GPIO LEDs (these same same as Pibrella)
#  RED    = BCM Port 27 = Pin 13
#  YELLOW = BCM Port 17 = Pin 11
#  GREEN  = BCM Port  4 = Pin  7
LED_RED=27

# Setup some constants for our world
# This is the RED mat:
HOME_X_RED = 33
HOME_Y_RED = 0
HOME_Z_RED = -32

# Setup the GPIO ports:
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)

# Subroutine to flash red:
def flash_red(t):
    GPIO.output(LED_RED, True)
    time.sleep(t)
    GPIO.output(LED_RED, False)
    time.sleep(t)

try:
    while True:
        pos = mc.player.getTilePos()
        if pos.x == HOME_X_RED and pos.z == HOME_Z_RED:
            flash_red(0.5)
finally:
    GPIO.cleanup()
