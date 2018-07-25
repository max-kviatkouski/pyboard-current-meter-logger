#!/usr/bin/env python3
from datetime import timezone, datetime, timedelta
import time

PYBOARD_EPOCH = datetime(2000, 1, 1, tzinfo=timezone.utc)
POSIX_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
DELTA = (PYBOARD_EPOCH - POSIX_EPOCH).total_seconds()

offset = time.localtime().tm_gmtoff // 3600
tz = timezone(timedelta(hours=offset))

def convert_to_posix(data):
    new_data = list()
    for line in data:
        vals = line.split(',')
        if (vals[0]):
            vals[0] = datetime.fromtimestamp(float(vals[0]) + DELTA, tz).strftime('%Y-%m-%d %H:%M:%S')
            new_data.append(",".join(vals))
        else:
            new_data.appen(line)
    return new_data