Installation Notes for Raspberry Pis used for CoderDojo Sessions.

1) Downloaded image "2019-04-08-raspbian-stretch-full.img" from:
https://www.raspberrypi.org/downloads/raspbian/

Raspbian Stretch with desktop and recommended software
Version:April 2019
Release date:2019-04-08
Kernel version:4.14

2) Burnt IMG file to Master 8GB MicroSD card labeled as "00"
SanDisk Ultra
8GB Class 10

3) 1st boot:
Country: UK
Language: British English
Timezone: London
Password: password
Accept screen (no need to tick black border)
Connect to wifi & set country code = UK
Next to check and update software, rebooted

4) 2nd boot:
Under Preferences / Raspberry PI Configuration:
- Hostname to "pi00"
- Enable:
-- Camera
-- SSH
-- SPI - Used by pi-topHUB v1 / GPIO pins 19, 21, 23 and 26 for SPI communication
-- I2C - Used by pi-topSPEAKER v1 / GPIO pins 3 and 5 for I2C communication
Reboot

5) Add extra components to support PiTop hardware:
sudo apt install pt-devices

6) added the CoderDojo repository via:
cd /home/pi
git clone https://github.com/markcarline/CoderDojo CoderDojo

7) Set desktop image
/home/pi/CoderDojo/utils/updatedesktop.sh
+ set desktop wallpaper to "codeclub.jpg" should be in folder:
/usr/share/rpd-wallpaper

8) Setup some libraries for project05 - fourletter-phat
NOTE: See notes from: https://github.com/pimoroni/fourletter-phat
curl https://get.pimoroni.com/fourletterphat | bash

9) Setup some libraries for project08 - pibrella:
NOTE: See notes from: https://github.com/pimoroni/pibrella
curl -sS get.pimoroni.com/pibrella | bash

10) Change a few minor tweeks:
- Start "file manager" and change view perferences so that "view as detailed list"

11) Created backup of "00" MicroSD card image as:
CoderDoJo_Build_v4-01.img
