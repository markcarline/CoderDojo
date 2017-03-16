project01 - Parent Detector
~~~~~~~~~

Based on:
https://www.raspberrypi.org/learning/parent-detector/

Step 1: What we need:

- Raspberry Pi

- Raspberry Pi Offical Camera Module

- PIR type sensor (HC-SR501) from Amazon: 
https://www.amazon.co.uk/gp/product/B01H6DYCJI/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1
also see datasheet in folder 31227sc.pdf

- 3 x female to female jumper leads

Step 2: Connect PIR motion sensor

GND - Black  - GND
OUT - Yellow - GP4
VCC - Red    - 5V

Step 3: Test the PIR motion sensor

From Menu > Programming > Python3 (IDLE) open /home/pi/CoderDojo/project01/script01.py
F5 to run and check we see both:
	"Motion detected!"
and:
	"No Motion detected!"
when PIR detects movement.

Step 4: Setting up the camera
- Power off.
- Plug in the camera so that blue strip is same side as ethernet cable.
- Power on.
- In the "Raspberry Pi Configuration Tool" ensure camera is enabled in the "Interfaces" tab.  Reboot if needed.

Step 5: Recording to a file and playing back
See script "script03.py"
and playing back use:
omxplayer 2017-02-11_10.24.18.h264 -o hdmi
NOTE: Renaming to mp4 doesnt work!
TIP: Add "omxplayer %f -o hdmi" as a custom command line when opening files like these.