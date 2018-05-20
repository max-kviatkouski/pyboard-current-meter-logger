from ampy.pyboard import Pyboard, PyboardError, stdout_write_bytes
from serial import *
import select
from threading import Thread
from io import StringIO, TextIOBase

def write_line(str):
    print("This is the line: " + str)

class ByteBuffer():

    def __init__(self, line_callback=None):
        self.line_callback = line_callback
        self.idx = 0
        self.buf = bytearray()

    def write(self, bytes):
        for i in range(0, len(bytes)):
            b = bytes[i]
            if self.idx >= len(self.buf):
                self.buf.append(b)
            else:
                self.buf[self.idx] = b
            self.idx += 1
            if b == ord('\n'):
                if (self.line_callback):
                    self.line_callback(self.buf[0:self.idx - 1].decode('ascii'))
                self.idx = 0

byteBuffer = ByteBuffer(write_line)

def main():
    # try:
    #     serial = Serial('/dev/ttyACM0', baudrate=115200, interCharTimeout=1)
    #     print("Successfull connect!")
    # except OSError as e:
    #     print(e)
    # except IOError as e:
    #     print(e)
    # pass
    pyb_thread = Thread(target=launch_pyb_script)
    pyb_thread.start()

def launch_pyb_script():
    pyb = Pyboard('/dev/ttyACM0', wait=30)
    pyb.enter_raw_repl()
    print('Before exec')
    pyb.exec_raw(
        'i=0\nwhile True:\n    pyb.LED(1).on()\n    pyb.delay(200)\n    print("{} Toggled".format(i))\n    pyb.LED(1).off()\n    pyb.delay(200)\n    i+=1',
        data_consumer=data_consumer_console_printer)
    print('After exec')
    pyb.exit_raw_repl()
    print('Exited raw REPL')

def data_consumer_console_printer(data):
    byteBuffer.write(data)

if __name__ == "__main__":
    main()