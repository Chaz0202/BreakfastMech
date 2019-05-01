import RPi.GPIO as GPIO
import time

button1 = 5
button2 = 6
button3 = 13
button4 = 19
button5 = 26
button6 = 20

button_list = [button1, button2, button3, button4, button5, button6]

choiceA = ""
choiceB = ""

led1 = 27
led2 = 22
led3 = 23
led4 = 24
led5 = 18
led6 = 25

led_list = [led1, led2, led3, led4, led5, led6]

def button1_pushed(event):
	global choiceA
	choiceA = "button1"

def button2_pushed(event):
	global choiceA
	choiceA = "button2"

def button3_pushed(event):
	global choiceB
	choiceB = "button3"

def button4_pushed(event):
	global choiceB
	choiceB = "button4"


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(27, GPIO.HIGH)

GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button1, GPIO.RISING)
GPIO.add_event_detect(button2, GPIO.RISING)
GPIO.add_event_detect(button3, GPIO.RISING)
GPIO.add_event_detect(button4, GPIO.RISING)
GPIO.add_event_detect(button5, GPIO.RISING)

GPIO.add_event_callback(button1, button1_pushed)
GPIO.add_event_callback(button2, button2_pushed)
GPIO.add_event_callback(button3, button3_pushed)
GPIO.add_event_callback(button4, button4_pushed)

GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(led1, GPIO.HIGH)

def main():
	GPIO.wait_for_edge(button5, GPIO.RISING)
	print(choiceA, choiceB)

try:
	main()

finally:
	print("quitting")
	GPIO.cleanup()
