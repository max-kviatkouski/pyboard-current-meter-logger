import pyb
from util import *

# pyb.usb_mode('CDC+HID')

orange.on()
pyb.delay(1000)
switch_value = pyb.Switch()()
orange.off()

if switch_value:
	pyb.usb_mode('CDC+MSC')
	blink_led(green)
	pyb.main('cardreader.py')
else:
	pyb.usb_mode('CDC+HID')
	blink_led(red)
	pyb.main('datalogger.py')
