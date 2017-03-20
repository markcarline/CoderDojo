#!/bin/bash 
gpio -g mode 4 in
while [  1 = 1 ]; do
  clear
  echo Checking the status of the GPIO ports via command "gpio readall"
  gpio readall
  date
  sleep 0.3
done
