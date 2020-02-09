Installation Notes for Raspberry Pis used for CoderDojo Sessions.

1) Downloaded image "2020-02-05-raspbian-buster-full.img" from:
https://www.raspberrypi.org/downloads/raspbian/

Raspbian Buster with desktop and recommended software
Image with desktop and recommended software based on Debian Buster
Version:February 2020
Release date:2020-02-05
Kernel version:4.19
Size:2532 MB

2) Burnt IMG file to Master 8GB MicroSD card labeled as "00"
SanDisk Ultra
8GB Class 10

3) 1st boot:
Country: UK
Language: British English
Timezone: London
Password: password
Accept screen (no need to tick black border)
Connect to CODERDOJO wifi & set country code = UK
Next to check and update software (took about 5 mins), rebooted

4) 2nd boot:
Under Preferences / Raspberry PI Configuration:
- Hostname to "pi00"
- Enable:
-- Camera
-- SSH
-- SPI - Used by pi-topHUB v1 / GPIO pins 19, 21, 23 and 26 for SPI communication
-- I2C - Used by pi-topSPEAKER v1 / GPIO pins 3 and 5 for I2C communication
Reboot

5) Additional config + clean up via:
sudo raspi-config
NOTE: Expand root file system via:
- Advanced options - expand root file system
NOTE: File system needs clean (on a 8gb card this should give us 1Gb free on root) up so run:
sudo apt-get clean

6) Add extra components to support PiTop hardware:
sudo apt install pt-devices
NOTE: "y" to install additional packages

7) added the CoderDojo repository via:
cd /home/pi
git clone https://github.com/markcarline/CoderDojo CoderDojo

8) Set desktop image
/home/pi/CoderDojo/utils/updatedesktop.sh
+ set desktop wallpaper to "codeclub.jpg" should be in folder:
/usr/share/rpd-wallpaper

9) Restore example "3 door" world in minecraft
cd /home/pi/CoderDojo/utils
./resetworld.sh
+ start minecraft and check we only see one world and that world has three doors

10) Setup some libraries for project05 - fourletter-phat
NOTE: See notes from: https://github.com/pimoroni/fourletter-phat
cd /home/pi
curl https://get.pimoroni.com/fourletterphat | bash
NOTE: "y" to I2C, expand filesystem and full installation

11) Setup some libraries for project08 - pibrella:
NOTE: See notes from: https://github.com/pimoroni/pibrella
cd /home/pi
curl -sS get.pimoroni.com/pibrella | bash

12) Add MU for using the BBC Microbit
sudo apt-get install mu -y
NOTE: Taken from notes from here:
https://projects.raspberrypi.org/en/projects/getting-started-with-microbit
NOTE: As we're now on Buster and using the full image MU is preinstalled and install is not needed - Skipping step.

13) Change a few minor tweeks:
- Start "file manager" and change
  a) view perferences so that "view as detailed list"
  b) Preferences menu + Display + Always show full file names
- Open any text file and enable "word wrap"

14) Created backup of "00" MicroSD card image as:
CoderDoJo_Build_v6-01.img
