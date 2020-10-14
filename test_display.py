#!/usr/bin/python3
import sys
import os
from PIL import Image,ImageDraw,ImageFont
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
  sys.path.append(libdir)

import logging
import time
from waveshare_epd import epd2in13b_V3

logging.basicConfig(level=logging.DEBUG)

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
  time.sleep(20)

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