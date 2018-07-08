#!/usr/bin/env python3
from threading import Thread
from ampy.pyboard import Pyboard
import axes_to_angle as axes
import numpy as np

def write_line(str):
    # print(str.strip(), end='\r')
    values = str.strip().split(',')
    angle = axes.get_angle(
        np.array([int(values[0]), int(values[1]), int(values[2])])
    )
    print("X: {:<4}, Y: {:<4}, Z: {:<4}, oZ angle: {:<4}".format(values[0], values[1], values[2], angle), end='\r')

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
    pyb_thread = Thread(target=launch_pyb_script)
    pyb_thread.start()

def launch_pyb_script():
    pyb = Pyboard('/dev/ttyACM0', wait=30)
    pyb.enter_raw_repl()
    print('Before exec')
    with open('endless-accel-loop.py', 'rb') as f:
        pyfile = f.read()
        pyb.exec_raw(
            pyfile,
            data_consumer=data_consumer_console_printer)
    print('After exec')
    pyb.exit_raw_repl()
    print('Exited raw REPL')

def data_consumer_console_printer(data):
    byteBuffer.write(data)

if __name__ == "__main__":
    main()