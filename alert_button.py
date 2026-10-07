import time
import requests
import RPi.GPIO as GPIO
import os
from dotenv import load_dotenv

load_dotenv() #tell Python to look at the .env file
BOT_TOKEN = os.getenv("BOT_TOKEN") # get the BOT_TOKEN environment variable
CHAT_ID = os.getenv("CHAT_ID") # get the CHAT_ID environment variable

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            requests.post(
                  f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id":CHAT_ID, "text": "Someone pressed the alert button!"}
            )

            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()
