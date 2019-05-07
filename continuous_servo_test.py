import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65) #i2c address 1x41

kit.continuous_servo[1].throttle = 1 #full forward
time.sleep(1)
kit.continuous_servo[1].throttle = -1 #full backward
time.sleep(1)
kit.continuous_servo[1].throttle = 0 #stop
