import pyb

accel = pyb.Accel()

while True:
    pyb.LED(1).on()
    x, y, z = accel.filtered_xyz()
    print("{},{},{}".format(x, y, z))
    pyb.delay(20)
    pyb.LED(1).off()
    pyb.delay(20)
