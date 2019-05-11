import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65) #i2c address 1x41

for n in range(2):
	for i in range(4):
		kit.servo[3].angle = 170 #Rotate to 180 degrees
		time.sleep(.1)
		kit.servo[3].angle = 150 #Rotate to 0 degrees
		time.sleep(.1)
	time.sleep(1.5)
