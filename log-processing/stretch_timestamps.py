#!/usr/bin/env python3
from datetime import datetime, timedelta
import time

def load_corrections(filename):
    df = '(%Y, %m, %d, %H, %M, %S)'
    def get_date_string(line):
        return line.split(':')[-1].strip()
    with open(filename) as f:
        lines = f.readlines()
        start_utc = datetime.strptime(get_date_string(lines[0]), df)
        end_actual_utc = datetime.strptime(get_date_string(lines[-2]), df)
        end_expected_utc = datetime.strptime(get_date_string(lines[-1]), df)
        td_actual = end_actual_utc - start_utc
        td_expected = end_expected_utc - start_utc
        k = td_expected.total_seconds()  / td_actual.total_seconds()
        offset = time.localtime().tm_gmtoff // 3600
        start_local = start_utc + timedelta(hours=offset)
        return start_local, k

def correct(timestamp, start_, k):
    td = timestamp - start_
    correct_td = timedelta(seconds=round((td.total_seconds() * k)))
    correction = correct_td - td
    return timestamp + correction

def stretch_timestamps(data, correction_filename):
    new_data = list()
    if not correction_filename:
        print("Correction file was not specified. Assuming no correction needed.")
        new_data.extend(data)
    else:
        CSV_DF = '%Y-%m-%d %H:%M:%S'
        start, k = load_corrections(correction_filename)
        print("Stretch coefficient K = {}".format(k))
        print("Sync time t0 = {}".format(start))
        for line in data:
            t_ = datetime.strptime(line.split(',')[0], CSV_DF)
            t = correct(t_, start, k)
            vals = line.split(',')
            vals[0] = t.strftime(CSV_DF)
            new_data.append(','.join(vals))
    return new_data