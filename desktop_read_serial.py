import serial
import time
import pyautogui
from datetime import datetime
import threading

# set up the serial line
ser = serial.Serial('COM4', 115200, timeout=.1)
time.sleep(2)

fire_last = time.time()
left_last = time.time()
right_last = time.time()
up_last = time.time()
down_last = time.time()

not_fire = True
not_down = True
not_up = True
not_right = True
not_left = True

def Key_PRESS(key):
    pyautogui.keyDown(key)

def Key_RELEASE(key):
    pyautogui.keyUp(key)


try:
    while True:
        try:
            lines = ser.readline()
            print(lines)
            if(lines == b'FIRE\r\n'):
                dirw = 'z'
                threading.Thread(target=Key_PRESS, args=(dirw,)).start()
                fire_last = time.time()
                not_fire = False
            if(lines == b'UP\r\n'):
                dirw = 'up'
                threading.Thread(target=Key_PRESS, args=(dirw,)).start()
                up_last = time.time()
                not_up = False
            if(lines == b'DOWN\r\n'):
                dirw = 'down'
                threading.Thread(target=Key_PRESS, args=(dirw,)).start()
                down_last = time.time()
                not_down = False
            if(lines == b'LEFT\r\n'):
                dirw = 'left'
                threading.Thread(target=Key_PRESS, args=(dirw,)).start()
                left_last = time.time()
                not_left = False
            if(lines == b'RIGHT\r\n'):
                dirw = 'right'
                threading.Thread(target=Key_PRESS, args=(dirw,)).start()
                right_last = time.time()
                not_right = False
        except Exception as E:
            print(E)

        # process the keystrokes
        RightNOW = time.time()

        
        if(RightNOW - fire_last > .05 and not not_fire):
            not_fire = True
            print("Fire Stopped")
            dirw = 'z'
            threading.Thread(target=Key_RELEASE, args=(dirw,)).start()
        
        if(RightNOW - up_last > .05 and not not_up):
            not_up = True
            print("Up Stopped")
            dirw = 'up'
            threading.Thread(target=Key_RELEASE, args=(dirw,)).start()
        if(RightNOW - down_last > .05 and not not_down):
            not_down = True
            print("Down Stopped")
            dirw = 'down'
            threading.Thread(target=Key_RELEASE, args=(dirw,)).start()

        if(RightNOW - left_last > .05 and not not_left):
            dirw = 'left'
            threading.Thread(target=Key_RELEASE, args=(dirw,)).start()
            not_left = True
            print("left Stopped")
        if(RightNOW - right_last > .05 and not not_right):
            dirw = 'right'
            threading.Thread(target=Key_RELEASE, args=(dirw,)).start()
            not_right = True
            print("Right Stopped")


except KeyboardInterrupt:
    pass