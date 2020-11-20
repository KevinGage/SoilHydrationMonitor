#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

soil_input = 7
check_time = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(soil_input, GPIO.IN)

# main loop
while True:
  if GPIO.input(soil_input):
    print('Input was HIGH')
  else:
    print('Input was LOW')
  time.sleep(check_time)