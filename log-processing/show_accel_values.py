#!/usr/bin/env python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import pylab
from subprocess import call, Popen

filename = sys.argv[1]
df = pd.read_csv(filename, header=0, squeeze=True, parse_dates=True, index_col=0)
plt.plot(df.resample('5T').mean())
input("Please take a look at the plot and note time frame where you think buoy was still. Press <Enter> to proceed")
plt.suptitle("Please remember timeframe when you think buoy \nwas holding still and close this window to proceed", fontsize=24)
plt.show()
bounds = input('Please enter timeframe in following format:\nhh:mm - hh:mm\n')
t1 = bounds.split('-')[0].strip()
t2 = bounds.split('-')[1].strip()
df_still = df.between_time(t1, t2)
zero_vector = [round(v) for v in df_still.mean()]
print("Zero vector is {}".format(zero_vector))
plt.plot(df.resample('5T').mean())
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[0], zero_vector[0]])
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[1], zero_vector[1]])
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[2], zero_vector[2]])
plt.show()