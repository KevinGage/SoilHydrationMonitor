#!/usr/bin/python3
import sys
import os
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
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