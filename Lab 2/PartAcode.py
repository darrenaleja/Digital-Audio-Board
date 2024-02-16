'''Blink the on board LED Pico W pinouts only
Patrick Palmer Jan 2024'''
from machine import Pin, Timer, PWM

led = machine.Pin("LED", machine.Pin.OUT)
timer = machine.Timer()
led.on()

def blink(timer):
    led.toggle()

timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)

duty_cycle = 1    
    
pwm_input =  int((duty_cycle/100)*65535)

pwm = PWM ( Pin ( 11, Pin.OUT ) ) # GP15
pwm. freq ( 100000 ) # 100kHz
pwm. duty_u16 (pwm_input ) # duty 50% (65535/2)