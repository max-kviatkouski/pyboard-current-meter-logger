import sys
import numpy as np
from rtcvariabilitytest import SLEEP_PERIOD

def main():
    slope_arr = []
    c = 0
    for line in sys.stdin:
        slope_arr.append(float(line))
        c += 1
    slope_avg = np.average(slope_arr)
    for i in range(0, c):
        print(i * SLEEP_PERIOD * (slope_arr[i] - slope_avg))

if __name__ == "__main__":
    main()