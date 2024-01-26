'''
Darren Aleja - 301338298
Amraz Mangat - 301368895
'''
from machine import Pin, Timer
import time


timer = Timer()

# List for gpio pins
gpio_list = [0, 1, 2, 3, 4, 5, 6, 7]

# Initialize pin as output
gpio_pin = [Pin(pin, Pin.OUT) for pin in gpio_list]

# Initialize LED
led = machine.Pin("LED",Pin.OUT)

# Function to turn off all gpio pins
def turnoff():
    gpio_pin[0].off()
    gpio_pin[1].off()
    gpio_pin[2].off()
    gpio_pin[3].off()
    gpio_pin[4].off()
    gpio_pin[5].off()
    gpio_pin[6].off()
    gpio_pin[7].off()
 
# Turn on [x] pin 
def turnon(x):
    gpio_pin[x].on()

# Loop creating a Quasi-square wave with period
while (1):
    
    gpio_pin[6].on()
    time.sleep_ms(10)
    
    turnoff()
    gpio_pin[7].on()
    time.sleep_ms(10)
    
    turnoff()
    gpio_pin[6].on()
    time.sleep_ms(10)
    
    
    turnoff()
    time.sleep_ms(10)
      
    


