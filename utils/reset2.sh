echo Removing old CoderDojo folder ...
sudo rm -r -f /home/pi/CoderDojo

echo Restore backup of /home/pi/BACKUP as /home/pi/CoderDojo
cp -r /home/pi/BACKUP /home/pi/CoderDojo
