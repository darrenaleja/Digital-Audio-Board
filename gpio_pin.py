from machine import Pin, Timer

gpio = [0,1,2,3,4,5,6,7]

for pin in gpio
    
    led = Pin(pin,Pin.OUT)
    led.high()
    