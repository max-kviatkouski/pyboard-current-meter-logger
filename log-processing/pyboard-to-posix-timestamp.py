#!/usr/bin/env python3
import sys
from datetime import timezone, datetime, timedelta
import time

PYBOARD_EPOCH = datetime(2000, 1, 1, tzinfo=timezone.utc)
POSIX_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
DELTA = (PYBOARD_EPOCH - POSIX_EPOCH).total_seconds()

offset = time.localtime().tm_gmtoff // 3600
tz = timezone(timedelta(hours=offset))

def main():
    for line in sys.stdin:
        vals = line.split(',')
        if (vals[0]):
            vals[0] = str(datetime.fromtimestamp(float(vals[0]) + DELTA, tz))
            print(",".join(vals), end='')
        else:
            print(line, end='')

if __name__ == "__main__":
    main()