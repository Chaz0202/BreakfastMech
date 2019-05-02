import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

def main():
    while True:
        pwm_led = GPIO.PWM(18, 100) #pwm at pin 18 and frequency 100Hz
        pwm_led.start(0) #start pwm, on for 0% of cycle

        for dc in range(0,50,1):
            pwm_led.ChangeDutyCycle(dc) #brightens (increases % time on for one cycle)
            time.sleep(0.1)

        for dc in range(50,0,-1):
            pwm_led.ChangeDutyCycle(dc) #dims (decreases % time on for one cycle)
            time.sleep(0.1)

try:
    setup()
    main()

finally:
    print("exiting")
    GPIO.cleanup()
