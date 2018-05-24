import sys

from ampy.pyboard import Pyboard
from datetime import datetime
import time
from calibration_util import ByteBuffer
import re

SLEEP_PERIOD = 10
FILENAME = 'rtc_deviation.log.' + str(SLEEP_PERIOD)

class CalibrationTracker:
    def setT0(self, t0):
        self.t0 = t0

    def get_deviation_percent(self, real, expected):
        d_real = real - self.t0
        d_expected = expected - self.t0
        return d_expected.total_seconds() / d_real.total_seconds()

def write_to_console(data):
    print(data.decode('ascii'))

def write_to_buffer(data):
    buf.write(data)

calibration_tracker = CalibrationTracker()

def print_tracker_info(s):
    try:
        t1_str, t2_str = re.sub(r'[^0-9,:]','', s).split(':')
        t1_arr = t1_str.split(',')
        t2_arr = t2_str.split(',')
        def arr_to_date(arr):
            return datetime(int(arr[0]), int(arr[1]), int(arr[2]), int(arr[4]), int(arr[5]), int(arr[6]))
        with open(FILENAME, 'a+') as f:
            f.write(str(calibration_tracker.get_deviation_percent(arr_to_date(t1_arr), arr_to_date(t2_arr))) + '\n')
    except:
        print("Unexpected error:", sys.exc_info()[0])

buf = ByteBuffer(print_tracker_info)

def main():
    with open(FILENAME, 'w+') as f:
        pass
    pyb = Pyboard('/dev/ttyACM0')
    pyb.enter_raw_repl()
    t0 = datetime.today()
    calibration_tracker.setT0(t0)
    print('Syncing RTC and PC clock')
    pyb.exec_raw(
        "rtc = pyb.RTC()\n"
        "t = ({0},{1},{2},{3},{4},{5},{6},{7})\n"
        "rtc.datetime(t)\n"
        "".format(t0.year, t0.month, t0.day, t0.date().weekday() + 1, t0.hour, t0.minute, t0.second + 1, 0),
        data_consumer=write_to_console
    )
    while True:
        now = datetime.today()
        pyb.exec_raw(
            "rtc_time = pyb.RTC().datetime()\n"
            "t_expected = ({0},{1},{2},{3},{4},{5},{6},{7})\n"
            "print(str(rtc_time) + ':' + str(t_expected))".format(now.year, now.month, now.day, now.date().weekday() + 1, now.hour, now.minute, now.second + 1, 0),
            data_consumer=write_to_buffer
        )
        time.sleep(SLEEP_PERIOD)
    pyb.exit_raw_repl()
    print('Done!')

if __name__ == "__main__":
    main()