#!/usr/bin/python3

import sys
import os
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
  sys.path.append(libdir)

import logging
import time
from waveshare_epd import epd2in13b_V3

logging.basicConfig(level=logging.DEBUG)


def draw_ok(current_time):
  font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
  font60 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 60)

  HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
  HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
  drawblack = ImageDraw.Draw(HBlackimage)
  drawry = ImageDraw.Draw(HRYimage)

  drawblack.text((10, 0), f'Last Check: {current_time} ', font = font12, fill = 0)
  drawblack.text((10, 20), 'OK', font = font60, fill = 0)

  epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
  time.sleep(3)

def draw_dry(current_time):
  font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
  font60 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 60)

  HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
  HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
  drawblack = ImageDraw.Draw(HBlackimage)
  drawry = ImageDraw.Draw(HRYimage)

  drawry.rectangle([(0,0), (298,126)], fill = 0)
  drawry.text((10, 0), f'Last Check: {current_time} ', font = font12, fill = 1)
  drawry.text((10, 20), 'DRY', font = font60, fill = 1)

  epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
  time.sleep(3)

try:
  logging.info("Starting test")

  epd = epd2in13b_V3.EPD()
  logging.info("init and Clear")
  epd.init()
  epd.Clear()
  time.sleep(1)

  logging.info("Drawing Horizontal image...")
  # create horizontal image buffers
  HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
  HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
  drawblack = ImageDraw.Draw(HBlackimage)
  drawry = ImageDraw.Draw(HRYimage)

  # load a font
  font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)

  # draw on the buffers
  drawblack.text((10, 0), 'hello world black', font = font20, fill = 0)
  drawry.text((10, 30), 'hello world red', font = font20, fill = 0)

  # draw buffers on screen
  epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
  time.sleep(3)

  # get the current time
  now = datetime.now()
  current_time = now.strftime("%H:%M")

  # test the OK screen
  draw_ok(current_time)

  # test the DRY screen
  draw_dry(current_time)

  logging.info("Clear...")
  epd.init()
  epd.Clear()

  logging.info("Goto Sleep...")
  epd.sleep()
  epd.Dev_exit()

except IOError as e:
  logging.info(e)

except KeyboardInterrupt:
  logging.info("ctrl + c:")
  epd2in13b_V3.epdconfig.module_exit()
  exit()