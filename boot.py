import pyb

# pyb.usb_mode('CDC+HID')

def blink_led(led_number):
	for i in range(1,4):
		pyb.LED(led_number).on()
		pyb.delay(500)
		pyb.LED(led_number).off()
		pyb.delay(500)

pyb.LED(3).on()
pyb.delay(2000)
switch_value = pyb.Switch()()
pyb.LED(3).off()

if switch_value:
	pyb.usb_mode('CDC+MSC')
	blink_led(2)
else:
	pyb.usb_mode('CDC+HID')
	blink_led(1)
