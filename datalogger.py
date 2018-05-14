import pyb
from util import *

accel = pyb.Accel()
switch = pyb.Switch()

while True:
	if switch():
		pyb.delay(200)
        log = open('/sd/log.csv', 'w')

        while not switch():
            # t = pyb.millis()
            # x, y, z = accel.filtered_xyz()
            # log.write('{},{},{},{}\n'.format(t,x,y,z))
            blink_led(red)
            
        log.close()
        blink_led(blue)
        pyb.delay(200)