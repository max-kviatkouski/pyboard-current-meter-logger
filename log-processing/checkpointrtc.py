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
        "rtc_time = pyb.RTC().datetime()\n"
        "rtc_time_str = '({{0}}, {{1}}, {{2}}, {{3}}, {{4}}, {{5}})'.format(rtc_time[0], rtc_time[1], rtc_time[2], rtc_time[4], rtc_time[5], rtc_time[6])\n"
        "t_real = ({0},{1},{2},{3},{4},{5})\n"
        "with open('datetime.correction', 'a+') as f:\n"
        "    f.write('Current UTC RTC is:' + rtc_time_str + '\\n')\n"
        "    print('Current UTC RTC on Pyboard is:' + rtc_time_str)\n"
        "    f.write('Real UTC time is:' + str(t_real) + '\\n')\n"
        "    print('Real UTC time is:' + str(t_real))\n"
        "    f.flush()\n"
        "    f.close()\n"
        "".format(now.year, now.month, now.day, now.hour, now.minute, now.second + 1),
        data_consumer=write_to_console
    )
    pyb.exit_raw_repl()
    print('Done!')

if __name__ == "__main__":
    main()