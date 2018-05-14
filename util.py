import pyb

red = pyb.LED(1)
green = pyb.LED(2)
orange = pyb.LED(3)
blue = pyb.LED(4)

def blink_led(led, times = 3, delay = 200):
	for i in range(1,times + 1):
		led.on()
		pyb.delay(delay)
		led.off()
		pyb.delay(delay)