import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)



'''
USE THESE ONES AS NANO PC DOESNT WANT TO WORK WITH GPIO

raspberry pi

black ground = 6
white up = 3
blue down = 5
green left = 7
red right = 8
orange fire = 10
'''

while True: # Run forever
    if GPIO.input(10) == GPIO.LOW: # FIre Button
        print("FIRE")
    if GPIO.input(3) == GPIO.LOW: # Up Direction
        print("UP")
    if GPIO.input(5) == GPIO.LOW: # DOWN Direction
        print("DOWN")
    if GPIO.input(7) == GPIO.LOW: # LEFT Direction
        print("LEFT")
    if GPIO.input(8) == GPIO.LOW: # RIGHT Direction
        print("RIGHT")