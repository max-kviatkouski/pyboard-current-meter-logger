#!/usr/bin/env python3
from ampy.pyboard import Pyboard
from datetime import datetime

def write_to_console(data):
    print(data.decode('ascii'), end='')

def main():
    pyb = Pyboard('/dev/ttyACM0')
    pyb.enter_raw_repl()
    now = datetime.utcnow()
    print('Writing RTC correction checkpoint')
    pyb.exec_raw(
        "print('Test')\n"
        "rtc_time = pyb.RTC().datetime()\n"
        "t_real = ({0},{1},{2},{3},{4},{5},{6},{7})\n"
        "with open('datetime.correction', 'a+') as f:\n"
        "    f.write('Current UTC RTC is: ' + str(rtc_time) + '\\n')\n"
        "    print('Current UTC RTC on Pyboard is: ' + str(rtc_time))\n"
        "    f.write('Real UTC time is: ' + str(t_real) + '\\n')\n"
        "    print('Real UTC time is ' + str(t_real))\n"
        "    f.flush()\n"
        "    f.close()\n"
        "".format(now.year, now.month, now.day, now.date().weekday() + 1, now.hour, now.minute, now.second + 1, 0),
        data_consumer=write_to_console
    )
    pyb.exit_raw_repl()
    print('Done!')

if __name__ == "__main__":
    main()