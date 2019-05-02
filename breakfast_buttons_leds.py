import RPi.GPIO as GPIO
import time

#GPIO pins of the buttons (in BCM)
button1 = 5
button2 = 6
button3 = 13
button4 = 19
button5 = 26
button6 = 20

#list of all buttons
button_list = [button1, button2, button3, button4, button5, button6]

#breakfast choices
choiceA = ""
choiceB = ""

#GPIO pins of LEDs (in BCM)
led1 = 27
led2 = 22
led3 = 23
led4 = 24
led5 = 18
led6 = 25

#list of all LEDs
led_list = [led1, led2, led3, led4, led5, led6]

working = True #whether the machine is currently working, used to stop the machine
choice_made = False

def button1_pushed(event): #to be run when button 1 pushed
	global choiceA
	choiceA = "button1"
	GPIO.output(led2, GPIO.LOW) #turn off other bread choice LED
	GPIO.output(led1, GPIO.HIGH) #turn on associated LED

def button2_pushed(event): #to be run when button 2 pushed
	global choiceA
	choiceA = "button2"
	GPIO.output(led1, GPIO.LOW) #turn off other bread choice LED
	GPIO.output(led2, GPIO.HIGH) #turn on associated LED

def button3_pushed(event): #to be run when button 3 pushed
	global choiceB
	choiceB = "button3"
	GPIO.output(led4, GPIO.LOW) #turn off the other spread choice LED
	GPIO.output(led3, GPIO.HIGH) #turn on associated LED

def button4_pushed(event): #to be run when button 4 pushed
	global choiceB
	choiceB = "button4"
	GPIO.output(led3, GPIO.LOW) #turn off other spread choice LED
	GPIO.output(led4, GPIO.HIGH) #turn on associated LED

def button5_pushed(event): #to be run when button 5 pushed
	global choice_made
	choice_made = True
	global working
	global led5_pwm
	led5_pwm = GPIO.PWM(led5, 100)
	led5_pwm.start(0)
	while working == True:
		for dc in range(0,50,1):
			led5_pwm.ChangeDutyCycle(dc)
			time.sleep(.01)
		for dc in range(50, 0, -1):
			led5_pwm.ChangeDutyCycle(dc)
			time.sleep(.01)

GPIO.setmode(GPIO.BCM) #BCM pin numbering

GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup all buttons as input

#when button pushed declare an event
GPIO.add_event_detect(button1, GPIO.RISING)
GPIO.add_event_detect(button2, GPIO.RISING)
GPIO.add_event_detect(button3, GPIO.RISING)
GPIO.add_event_detect(button4, GPIO.RISING)
GPIO.add_event_detect(button5, GPIO.RISING)

#When event declared run a function
GPIO.add_event_callback(button1, button1_pushed)
GPIO.add_event_callback(button2, button2_pushed)
GPIO.add_event_callback(button3, button3_pushed)
GPIO.add_event_callback(button4, button4_pushed)
GPIO.add_event_callback(button5, button5_pushed)

#setup LEDs as output
GPIO.setup(led_list, GPIO.OUT, initial=GPIO.LOW)

def main():
	#buttons are pushed and variables save choices
	while choice_made == False:
		time.sleep(.1)
	print(choiceA, choiceB)
	time.sleep(4)

try:
	main()

finally:
	working = False
	print("quitting")
	GPIO.cleanup() #remove all pin setups
