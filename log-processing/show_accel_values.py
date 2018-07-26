#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import pandas as pd
import os

#load data
filename = sys.argv[1]
df = pd.read_csv(filename, header=0, squeeze=True, parse_dates=True, index_col=0)

#coarse grain it and make smoother by averaging
plt.plot(df.resample('5T').mean())

#show smoothed raw data to let user pick 'still water' timeframe
input("Please take a look at the plot and note time frame where you think buoy was still. Press <Enter> to proceed")
plt.suptitle("Please remember timeframe when you think buoy \nwas holding still and close this window to proceed", fontsize=24)
plt.show()

#calculate average of accelerometer during 'still water' timeframe and take it as vector of 'zero position'
bounds = input('Please enter timeframe in following format:\nhh:mm - hh:mm\n')
t1 = bounds.split('-')[0].strip()
t2 = bounds.split('-')[1].strip()
df_still = df.between_time(t1, t2)
zero_vector = [round(v) for v in df_still.mean()]
print("Zero vector is {}".format(zero_vector))

#plot smoothed raw data + lines for 'zero' values of accelerometer
plt.plot(df.resample('5T').mean())
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[0], zero_vector[0]])
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[1], zero_vector[1]])
plt.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[2], zero_vector[2]])
plt.suptitle('Please close to proceed', fontsize=24)
plt.show()

#save zero vector into a corresponding file
dir = os.path.dirname(filename)
zero_vector_filename = os.path.join(dir, "{}.zero".format(os.path.basename(filename)))
print('Saving zero vector into {}'.format(zero_vector_filename))
with open(zero_vector_filename, 'w+') as zf:
    zf.write(str(zero_vector))