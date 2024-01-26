'''
Darren Aleja - 301338298
Amraz Mangat - 301368895
'''
from machine import Pin, Timer


timer = Timer()

# List for gpio pins
gpio_list = [0, 1, 2, 3, 4, 5, 6, 7]

# Initialize pin as output
gpio_pin = [Pin(pin, Pin.OUT) for pin in gpio_list]

# Initialize LED
led = machine.Pin("LED",Pin.OUT)

# Turn on Pin and LED
gpio_pin[7].on()
led.on()


def  blinky(timer):
    gpio_pin[7].toggle()
    led.toggle()

timer.init(freq=10,mode=Timer.PERIODIC,callback=blinky)