#!/usr/bin/env python3
import numpy as np
import sys

SIZE = 50
CONV_CORE = np.ones((SIZE,)) / SIZE

def main():
    all_rows = [l.split(',') for l in sys.stdin]
    all_x = [float(r[1]) for r in all_rows]
    all_y = [float(r[2]) for r in all_rows]
    all_z = [float(r[3]) for r in all_rows]

    averaged_x = np.convolve(all_x, CONV_CORE, mode='valid')
    averaged_y = np.convolve(all_y, CONV_CORE, mode='valid')
    averaged_z = np.convolve(all_z, CONV_CORE, mode='valid')

    for i, _ in enumerate(averaged_x):
        print("{},{},{},{}".format(all_rows[i][0], averaged_x[i], averaged_y[i], averaged_z[i]))

if __name__ == "__main__":
    main()