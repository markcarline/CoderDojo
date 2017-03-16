#!/bin/bash 
while [  1 = 1 ]; do
  clear
  echo Checking the status of the GPIO ports via command "gpio readall"
  gpio readall
  date
  wait 0.2
done
