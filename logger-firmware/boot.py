import pyb
from util import *

orange.on()
pyb.delay(1000)
switch = pyb.Switch()
switch_value = switch.value()
orange.off()
# 0 press nothing - go to standby mode (good for pre-deployment) (single red blinker)
# 1 press USR shortly and let go - sampling (orange blinker)
# 2 press USR and keep - go to cardreader mode (single green blinker)
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
	#disable wakeup trigger that might've been left from previous setup
	rtc = pyb.RTC()
	rtc.wakeup(None)
	blink_led(red)
	pyb.standby()