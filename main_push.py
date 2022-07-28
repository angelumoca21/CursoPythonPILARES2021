from machine import Pin

LED = Pin(22,Pin.OUT)
BOTON = Pin(21,Pin.IN)

while True:
    if (BOTON.value() == 1):
        LED.value(0)
    else:
        LED.value(1)