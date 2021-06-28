import sys, traceback

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
b = nxt.locator.find_one_brick()

print("AIDS")



m_left = Motor(b, PORT_B)
m_left.turn(100, 20)