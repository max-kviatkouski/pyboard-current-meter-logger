import sys
import numpy as np
from numpy.linalg import norm
from math import acos, degrees

STRAIGHT_UP_VECTOR = np.array([0, 0, 1])

def get_angle(v):
    dot_product = np.dot(v, STRAIGHT_UP_VECTOR)
    length_product = norm(v) * norm(STRAIGHT_UP_VECTOR)
    return degrees(acos(dot_product / length_product))

def main():
    for line in sys.stdin:
        row = line.split(',')
        t = row[0]
        g_vector = np.array([float(i) for i in row[1:]])
        angle = get_angle(g_vector)
        print("{},{}".format(t, angle))

if __name__ == "__main__":
    main()