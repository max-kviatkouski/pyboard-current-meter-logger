import pyb
from util import *
import utime

#data frames in ms
DELAY_BETWEEN_CYCLES = 60 * 1000
#sampling frequency within frame in Hz
FREQ = 10
#frame duration in ms
DURATION = 2000
_in_frame_delay = 1000 // FREQ
_n = DURATION // _in_frame_delay
accel = pyb.Accel()
switch = pyb.Switch()
rtc = pyb.RTC()
rtc.wakeup(DELAY_BETWEEN_CYCLES)
datetime = rtc.datetime()
filename = "/sd/log.{}-{:0>2}-{:0>2}.csv".format(datetime[0], datetime[1], datetime[2])

def log_series():
    with open(filename, 'a+') as log:
        for i in range(0, _n):
            t = utime.time()
            x, y, z = accel.filtered_xyz()
            log.write('{},{},{},{}\n'.format(t, x, y, z))
            pyb.delay(_in_frame_delay)

while True:
    if switch.value():
        blink_led(blue, 2, 20)
        break
    log_series()
    blink_led(orange, 2, 20)
    pyb.stop()