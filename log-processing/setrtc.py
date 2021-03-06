#!/usr/bin/env python3
from ampy.pyboard import Pyboard
from datetime import datetime

def write_to_console(data):
    print(data.decode('ascii'), end='')

def main():
    pyb = Pyboard('/dev/ttyACM0')
    pyb.enter_raw_repl()
    now = datetime.utcnow()
    print('Setting UTC time')
    pyb.exec_raw(""
        "import sys\n"
        "rtc = pyb.RTC()\n"
        "rtc.init()\n"
        "t_py = ({0},{1},{2},{3},{4},{5},{6},{7})\n"
        "t = '({0}, {1}, {2}, {4}, {5}, {6})'\n"
        "rtc.datetime(t_py)\n"
        "print('UTC Time now is:')\n"
        "print(rtc.datetime())\n"
        "try:\n"
        "   with open('datetime.correction', 'a+') as f:\n"
        "       f.write('Initialized UTC RTC with:' + t + '\\n')\n"
        "       f.flush()\n"
        "       f.close()\n"
        "       print('Done writing to file')\n"
        "except Exception as exc:\n"
        "   sys.print_exception(exc)\n"
        "print('PyBoard execution finished.')\n"
        "".format(now.year, now.month, now.day, now.date().weekday() + 1, now.hour, now.minute, now.second + 1, 0),
        data_consumer=write_to_console
    )
    pyb.exit_raw_repl()
    print('Done!')

if __name__ == "__main__":
    main()
