#!/usr/bin/python3
### Change These ###
# Io for hydration sensor
soil_input = 7

# Time between checks in seconds
check_time = 1800

#MQTT broker address and credentials
Broker = ''
auth = {
    'username': '',
    'password': '',
}
mqtt_port = 8883

### Dont change after this line ###

# import libraries
import os
import sys
import signal
import RPi.GPIO as GPIO
import time
from datetime import datetime
import atexit
from PIL import Image,ImageDraw,ImageFont
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
  sys.path.append(libdir)
from waveshare_epd import epd2in13b_V3

# setup gpio input for sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil_input, GPIO.IN)

# setup display
epd = epd2in13b_V3.EPD()
epd.init()
epd.Clear()

# display cleanup on interupt exit
def signal_handler(sig, frame):
  print('caught interupt')
  print('clearing display')
  epd.Clear()
  time.sleep(10)
  epd2in13b_V3.epdconfig.module_exit()
  print('exiting')
  sys.exit()
signal.signal(signal.SIGINT, signal_handler)

# import some fonts
font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
font60 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 60)

def draw_ok(current_time):
  HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
  HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
  drawblack = ImageDraw.Draw(HBlackimage)
  drawry = ImageDraw.Draw(HRYimage)

  # drawblack.text((10, 0), f'Last Check: {current_time} ', font = font12, fill = 0)
  # drawblack.text((10, 20), 'OK', font = font60, fill = 0)
  drawblack.text((10, 20), current_time, font = font60, fill = 0)

  epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

def draw_dry(current_time):
  HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
  HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
  drawblack = ImageDraw.Draw(HBlackimage)
  drawry = ImageDraw.Draw(HRYimage)

  drawry.rectangle([(0,0), (298,126)], fill = 0)
  # drawry.text((10, 0), f'Last Check: {current_time} ', font = font12, fill = 1)
  # drawry.text((10, 20), 'DRY', font = font60, fill = 1)
  drawry.text((10, 20), current_time, font = font60, fill = 1)

  epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

### Main Function ###
while True:
  now = datetime.now()
  current_time = now.strftime("%H:%M")

  if GPIO.input(soil_input):
    draw_dry(current_time)
  else:
    draw_ok(current_time)

  time.sleep(check_time)