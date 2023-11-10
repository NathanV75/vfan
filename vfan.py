#!/usr/bin/python3
import pigpio
import time

CPU_TEMP='/sys/class/thermal/thermal_zone0/temp'

LOW_TEMP = 60.0
MID_TEMP = 70.0
HIGH_TEMP = 73.0
MAX_TEMP = 77.0

OFF_DUTY = 0
LOW_DUTY = 610000
MID_DUTY = 870000
HIGH_DUTY = 950000
MAX_DUTY = 1000000

PWM_FREQ = 25000

FAN_GPIO = 18

PARAMS = [(LOW_TEMP, LOW_DUTY), (MID_TEMP, MID_DUTY), (HIGH_TEMP, HIGH_DUTY), (MAX_TEMP, MAX_DUTY)]

USE_PWM = True
TEST = False

def get_cpu_temp() -> float:
    return float(open(CPU_TEMP, 'r').readline()) / 1000

def get_duty_cycle(temperature: float) -> int:
    duty = OFF_DUTY
    for (t, d) in PARAMS:
        if temperature >= t:
            duty = d
    return duty

def pwm_loop():
    """
    Adjust fan speed with PWM. Sets fan speed based on PARAMS.
    """
    pi = pigpio.pi()
    print("Starting PWM fan...")
    try:
        while pi.connected:
            pi.hardware_PWM(FAN_GPIO, PWM_FREQ, get_duty_cycle(get_cpu_temp()))
            time.sleep(5)
    except KeyboardInterrupt:
        print("Terminated")
    pi.hardware_PWM(FAN_GPIO, 0, 0)

def pwm_test():
    """
    Cycles through fan speeds in PARAMS. Use to check noise levels.
    """
    pi = pigpio.pi()
    print("Starting PWM test...")
    try:
        while pi.connected:
            for t, duty in [(0,OFF_DUTY)] + PARAMS:
                pi.hardware_PWM(FAN_GPIO, PWM_FREQ, duty)
                print(duty)
                time.sleep(10)
    except KeyboardInterrupt:
        print("Terminated")
    pi.hardware_PWM(FAN_GPIO, 0, 0)

def toggle_loop():
    """
    Toggles the fan on and off. Turns on at MAX_TEMP and stays on until it cools to MIN_TEMP.
    """
    pi = pigpio.pi()
    print("Starting dynamic fan...")
    fan_on = False
    try:
        while True:
            temp = get_cpu_temp()
            if temp >= MAX_TEMP:
                pi.write(FAN_GPIO, 1)
                fan_on = True
            elif fan_on and temp < MIN_TEMP:
                pi.write(FAN_GPIO, 0)
                fan_on = False
            time.sleep(5)
    except KeyboardInterrupt:
        print("Terminated")

if __name__ == "__main__":
    if TEST:
        pwm_test()
    elif USE_PWM:
        pwm_loop()
    else:
        toggle_loop()
