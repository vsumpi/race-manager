## BiFrost by Varga Zsombor, 2023 C
## For Raspbery Pi Zero 2 W
## Libraries:
## RPi.GPIO: https://pypi.org/project/RPi.GPIO/
## Matrix https://github.com/hzeller/rpi-rgb-led-matrix
## Used ChatGPT May3 Version.

import time
import sys
import datetime
import os
import threading
import RPi.GPIO as GPIO
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# GPIO settings for the button:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Matrix flags:
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.drop_privileges = False

# Graphics settings:
matrix = RGBMatrix(options=options)
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")
red = graphics.Color(255, 0, 0)

# Global variables:
gapRacer = 30

# Buffer for time
time_buffer = []

# Thread to check for button press
def button_thread():
    while True:
        if GPIO.input(35) == GPIO.HIGH:
            time_buffer.append(datetime.datetime.now().strftime("%H:%M:%S"))
            time.sleep(0.5)

# Start button thread
button = threading.Thread(target=button_thread)
button.start()

# Functions:
def Clear():
    matrix.Clear()

def Clock():
    Clear()
    # Set the clock to current time
    clock = datetime.datetime.now()
    hours = clock.strftime("%H")
    minutes = clock.strftime("%M")
    seconds = clock.strftime("%S")
    print("Time: {}:{}:{}".format(hours, minutes, seconds), end="\r")
    graphics.DrawText(matrix, font, 3, 10, red, "{}:{}:{}".format(hours, minutes, seconds))
    Gap(seconds)
    time.sleep(1)
    return hours, minutes, seconds

def Gap(seconds):
    try:
        gap = abs((int(seconds) % gapRacer) - gapRacer)
        graphics.DrawText(matrix, font, 15, 26, red, ":{}".format(gap))
    except ZeroDivisionError:
        print("Error")

while True:
    Clear()
    Clock()
    # Save time buffer to file when GPIO 35 is pressed or rising edge
    if time_buffer:
        with open("time_log.txt", "a") as f:
            f.write("\n".join(time_buffer) + "\n")
            time_buffer.clear()
