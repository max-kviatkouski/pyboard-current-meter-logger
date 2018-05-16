import sys

def main():
    c = 0
    for line in sys.stdin:
        row = line.split(',')
        if (row[0]):
            #dump prev values
            if (c):
                print("{},{},{},{}".format(t, x/c, y/c, z/c))
            #reset accumulators
            t, x, y, z, c = row[0], 0, 0, 0, 0
        #keep accumulating
        x += int(row[1])
        y += int(row[2])
        z += int(row[3])
        c += 1

if __name__ == "__main__":
    main()