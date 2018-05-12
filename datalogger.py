import pyb

def blink_led(led_number):
	for i in range(1,4):
		pyb.LED(led_number).on()
		pyb.delay(500)
		pyb.LED(led_number).off()
		pyb.delay(500)

accel = pyb.Accel()
red = pyb.LED(1)
switch = pyb.Switch()

log = open('/sd/log.csv', 'w')
t = pyb.millis()
x, y, z = accel.filtered_xyz()
log.write('{},{},{},{}\n'.format(t,x,y,z))
log.close()

blink_led(4)