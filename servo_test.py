import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65) #i2c address 1x41

kit.servo[0].angle = 90 #Rotate to 180 degrees
time.sleep(1)
kit.servo[0].angle = 60 #Rotate to 0 degrees
