import pyb
from util import *

DELAY_BETWEEN_CYCLES = 5000
accel = pyb.Accel()
switch = pyb.Switch()
rtc = pyb.RTC()
rtc.wakeup(DELAY_BETWEEN_CYCLES)



def log_series(delay = 20, duration = 5000):
    with open('/sd/log.csv', 'a+') as log:
        n = duration // delay
        t = pyb.millis()
        x, y, z = accel.filtered_xyz()
        log.write('{},{},{},{}\n'.format(t, x, y, z))
        for i in range(2, n+1):
            x, y, z = accel.filtered_xyz()
            log.write(',{},{},{}\n'.format(x, y, z))

def log_file_header():
    with open('/sd/log.csv', 'a+') as log:
        log.write('Time,X,Y,Z\n')

log_file_header()
while True:
    log_series()
    blink_led(red)
    if switch():
        blink_led(blue)
        break
    pyb.standby()