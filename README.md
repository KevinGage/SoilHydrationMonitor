# SoilHydrationMonitor
Monitor soil hydration with a raspberry pi and eink display

# Components

sensor: https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial

display: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(B)

raspberry pi zero w

# Setup
## Enable SPI on Pi
```sudo raspi-config```
Choose Interfacing Options -> SPI -> Yes  to enable SPI interface

## Install libraries
```
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
```