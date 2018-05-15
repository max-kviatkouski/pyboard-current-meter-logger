import pyb
from util import *

accel = pyb.Accel()
switch = pyb.Switch()

DELAY_BETWEEN_CYCLES = 5000

def log_series(delay = 20, duration = 5000):
    with open('/sd/log.csv', 'a+') as log:
        n = duration // delay
        for i in range(1, n+1):
            t = pyb.millis()
            x, y, z = accel.filtered_xyz()
            log.write('{},{},{},{}\n'.format(t, x, y, z))

while True:
    log_series()
    blink_led(red)
    pyb.delay(DELAY_BETWEEN_CYCLES)
    if switch():
        blink_led(blue)
        break
