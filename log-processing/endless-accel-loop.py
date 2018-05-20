import pyb

accel = pyb.Accel()

while True:
    x, y, z = accel.filtered_xyz()
    print("{<5}{<5}{<5}".format(x, y, z), end='\r')