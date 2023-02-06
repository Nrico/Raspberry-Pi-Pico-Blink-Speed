"""Example for Pico. Turns on the built-in LED and blinks slowly at first, then speeds up"""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT



for i in range(5, 60):
    led.value = True
    time.sleep(1/i)
    led.value = False
    time.sleep(1/i)
