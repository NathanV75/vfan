#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

CPU_TEMP='/sys/class/thermal/thermal_zone0/temp'

MAX_TEMP = 77.0
MIN_TEMP = 60.0
MAX_DUTY = 100
MIN_DUTY = 30
OFF_DUTY = 0
PWM_FREQ = 10
FAN_GPIO = 18

def get_cpu_temp() -> float:
    return float(open(CPU_TEMP, 'r').readline()) / 1000

def calculate_duty_cycle(temperature: float) -> int:
    print(temperature)
    duty = 0
    if temperature >= MAX_TEMP:
        duty = MAX_DUTY
    elif temperature <= MIN_TEMP:
        duty = OFF_DUTY
    else:
        duty = round((temperature - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * (MAX_DUTY - MIN_DUTY) + MIN_DUTY)
    print(duty)
    return duty


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_GPIO, GPIO.OUT)
    pwm = GPIO.PWM(FAN_GPIO, PWM_FREQ)
    print("Starting fan...")
    pwm.start(calculate_duty_cycle(get_cpu_temp()))
    try:
        while True:
            time.sleep(5)
            pwm.ChangeDutyCycle(calculate_duty_cycle(get_cpu_temp()))
    except KeyboardInterrupt:
        print("Terminated")
    GPIO.cleanup()
