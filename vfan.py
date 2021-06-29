#!/usr/bin/python3
from gpiozero import CPUTemperature
import pigpio

MAX_TEMP = 77.0
MIN_TEMP = 70.0
MAX_DUTY = 255
MIN_DUTY = 100
OFF_DUTY = 0
PWM_FREQ = 10
FAN_GPIO = 4

pi = pigpio.pi()
if pi.connected:
    cpu = CPUTemperature()

    f = open("temp.log", 'a')
    f.write("{}\n".format(cpu.temperature))
    f.close()

    duty = 0
    if cpu.temperature >= MAX_TEMP:
        duty = MAX_DUTY
    elif cpu.temperature <= MIN_TEMP:
        duty = OFF_DUTY
    else:
        duty = (cpu.temperature - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * (MAX_DUTY - MIN_DUTY) + MIN_DUTY

    pi.set_PWM_frequency(FAN_GPIO, PWM_FREQ)
    pi.set_PWM_dutycycle(FAN_GPIO, duty)
else:
    f = open("temp.log", 'a')
    f.write("No pigpiod...,\n")
    f.close()
