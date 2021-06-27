from gpiozero import LED, Button
from signal import pause

button = Button(10)

button.when_pressed = print("ONN")
button.when_released = print("OFF")
