#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
oldid=""

try:
    while True:
            print("Now place your tag to read")
            id, text = reader.read()
            print(id)
            print(text)
finally:
        GPIO.cleanup()
