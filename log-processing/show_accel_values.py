import pandas as pd
import matplotlib
import sys
import matplotlib.pyplot as plt

filename = sys.argv[1]
df = pd.read_csv(filename, header=0, squeeze=True, parse_dates=True, index_col=0)
df.resample('5T').mean().plot()
# matplotlib.use('TkAgg')
# df.plot(linewidth=1)
plt.ion()
plt.show(block = False)
plt.pause(0.001)
bounds = input('Enter time period when you think there was no current at all in a form of hh:mm - hh:mm\n')
t1 = bounds.split('-')[0].strip()
t2 = bounds.split('-')[1].strip()
df_still = df.between_time(t1, t2)
zero_vector = [round(v) for v in df_still.mean()]
print("Zero vector is {}".format(zero_vector))
f, ax = plt.subplots(1)
ax.plot([df.first_valid_index(), df.last_valid_index()], [zero_vector[0], zero_vector[0]])
