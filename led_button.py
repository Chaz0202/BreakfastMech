import RPi.GPIO as GPIO

def button_pushed(event):
        if GPIO.input(18) == 0:
                GPIO.output(18, GPIO.HIGH)
        else:
                GPIO.output(18, GPIO.LOW)
        print("yee")

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(5, GPIO.RISING, callback=button_pushed)
	GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

try:
	setup()
	message = input("Press <ENTER> to quit")

finally:
	print("quitting")
	GPIO.cleanup()

