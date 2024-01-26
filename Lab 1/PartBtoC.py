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
led.on()

def turnoff():
    gpio_pin[0].off()
    gpio_pin[1].off()
    gpio_pin[2].off()
    gpio_pin[3].off()
    gpio_pin[4].off()
    gpio_pin[5].off()
    gpio_pin[6].off()
    gpio_pin[7].off()
    
def turnon(x):
    gpio_pin[x].on()

def  blinky(timer):
    led.toggle()

timer.init(freq=10,mode=Timer.PERIODIC,callback=blinky)