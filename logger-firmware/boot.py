import pyb
from util import *

orange.on()
pyb.delay(1000)
switch = pyb.Switch()
switch_value = switch.value()
orange.off()

if switch_value:
	blue.on()
	pyb.delay(1000)
	switch_value = switch.value()
	blue.off()
	if switch_value:
		pyb.usb_mode('CDC+MSC')
		blink_led(green)
		pyb.main('cardreader.py')
	else:
		pyb.usb_mode('CDC+HID')
		blink_led(orange)
		pyb.main('datalogger.py')
else:
	blink_led(red)
	pyb.standby()