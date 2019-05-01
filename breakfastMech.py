from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time

white_bread = 5
whole_wheat_bread = 6
bread_choice = ""

jam_spread = 13
honey_spread = 19
spread_choice = ""

abort = 20

def GPIO_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(5, GPIO.RISING, callback=white_bread)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(6, GPIO.RISING, callback=whole_wheat_bread)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(13, GPIO.RISING, callback=jam_spread)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(19, GPIO.RISING, callback=honey_spread)

def white_bread(event):
	global bread_choice
	bread_choice = "white bread"
	print("yee")

def whole_wheat_bread(event):
	global bread_choice
	bread_choice = "whole wheat"

def jam_spread(event):
	global spread_choice
	spread_choice = "jam"

def honey_spread(event):
	global spread_choice
	spread_choice = "honey"

kit = ServoKit(channels=16, address=65) #i2c address 1x41

kit.continuous_servo[0].throttle = 1 #full forward
time.sleep(1)
kit.continuous_servo[0].throttle = -1 #full backward
time.sleep(1)
kit.continuous_servo[0].throttle = 0 #stop

message = input("Whats for Break")
print(bread_choice, spread_choice)
