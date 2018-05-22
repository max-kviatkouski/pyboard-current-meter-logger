from ampy.pyboard import Pyboard
from datetime import datetime

def write_to_console(data):
    print(data.decode('ascii'), end='')

def main():
    pyb = Pyboard('/dev/ttyACM0')
    pyb.enter_raw_repl()
    now = datetime.today()
    print('Setting time')
    pyb.exec_raw(
        "rtc = pyb.RTC()\nrtc.datetime(({},{},{},{},{},{},{},{}))\nprint('Time now is:')\nprint(rtc.datetime())".format(now.year, now.month, now.day, now.date().weekday() + 1, now.hour, now.minute, now.second + 1, 0),
        data_consumer=write_to_console
    )
    pyb.exit_raw_repl()
    print('Done!')

if __name__ == "__main__":
    main()