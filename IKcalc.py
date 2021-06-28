import sys, traceback
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

if '--help' in sys.argv:
    print("""Tests the nxt-python setup and brick firmware interaction
Usage: nxt_test           # Finds one brick and shows information about it
       nxt_test --verbose # Shows more debug information when trying to find the brick
       nxt_test --help    # Shows this help
""")
    exit(0)

import nxt
import nxt.locator
import nxt.brick
import nxt.usbsock

#nxt.locator.make_config()
from nxt.motor import *
debug = False
if '--verbose' in sys.argv or '--debug' in sys.argv:
    debug = True
    print('debug = True')

b = None
try:
    print('Find brick...', flush=True)
    b = nxt.locator.find_one_brick(debug=True)
    name, host, signal_strength, user_flash = b.get_device_info()
    print('NXT brick name: %s' % name)
    print('Host address: %s' % host)
    print('Bluetooth signal strength: %s' % signal_strength)
    print('Free user flash: %s' % user_flash)
    prot_version, fw_version = b.get_firmware_version()
    print('Protocol version %s.%s' % prot_version)
    print('Firmware version %s.%s' % fw_version)
    millivolts = b.get_battery_level()
    print('Battery level %s mV' % millivolts)
    print('done')
except:
    print("Error while running test:")
    traceback.print_tb(sys.exc_info()[2])
    print(str(sys.exc_info()[1]))
    if b in locals():
        b.sock.close()

base_motor = Motor(b, PORT_B)

print("READY!!")

while True: # Run forever
    if GPIO.input(10) == GPIO.LOW: # FIre Button
        print("FIRE")
    if GPIO.input(3) == GPIO.LOW: # Up Direction
        print("UP")
    if GPIO.input(5) == GPIO.LOW: # DOWN Direction
        print("DOWN")
    if GPIO.input(7) == GPIO.LOW: # LEFT Direction
        print("LEFT")
        base_motor.turn(-50, 10)
    if GPIO.input(8) == GPIO.LOW: # RIGHT Direction
        print("RIGHT")
        base_motor.turn(50, 10)