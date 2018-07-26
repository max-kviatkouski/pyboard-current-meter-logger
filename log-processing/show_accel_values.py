import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import pylab
from subprocess import call, Popen

filename = sys.argv[1]
df = pd.read_csv(filename, header=0, squeeze=True, parse_dates=True, index_col=0)
# df.resample('5T').mean().plot()
# pylab.savefig('test.png', dpi = 600)
# Popen("xdg-open", "test.png", shell=False)
# plt.show(block = False)
# plt.pause(0.001)
# bounds = input('Enter time period when you think there was no current at all in a form of hh:mm - hh:mm\n')
bounds = "05:00 - 11:00"
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