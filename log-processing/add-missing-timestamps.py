#!/usr/bin/env python3

#this script will simply repeat same timestamp for all records in a measurement frame to make csv processing easier

import sys
from stretch_timestamps import stretch_timestamps
from pyboard_to_posix_timestamp import convert_to_posix
import pandas as pd
from io import StringIO

#load files and add timestamps (may need to be removed in the future - I can just add timestamps by logger itself)
csv_filenames = sys.argv[1:-2]
data = list()
for filename in csv_filenames:
    print("Loading {}".format(filename))
    ts = ''
    with open(filename, "r") as f:
        for l in f.readlines():
            vals = l.split(',')
            if vals[0]:
                ts = vals[0]
            elif ts:
                vals[0] = ts
            new_line = ','.join(vals)
            data.append(new_line)

#convert PyBoard timestamps to POSIX
local_time_data = convert_to_posix(data)

#stretch time based on correction file. filename of correction data should be the last argument passed
stretched_log = ["Time,Xacc,Yacc,Zacc\n"] #header
stretched_log.extend(stretch_timestamps(local_time_data, sys.argv[-2]))

#save updated log data into files grouped by day
#use pandas to manipulate dataset
target_folder = sys.argv[-1]
CSV_DF = '%Y-%m-%d %H:%M:%S'
str_io = StringIO(''.join(stretched_log)) #lines already have end of new line in the end
dframe = pd.read_csv(str_io, header=0, index_col=0, parse_dates=True, infer_datetime_format=True)
print(dframe.size)