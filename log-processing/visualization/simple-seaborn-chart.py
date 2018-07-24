import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def data_parser(dstring):
    s = dstring[0]
    d = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    return d

def main():
    series = pd.read_csv('../../../pyboard-current-meter-logger-data/log.2018-07-20.fixed-time.csv',
                         header=None, index_col=0, squeeze=True, parse_dates=True)
    series.resample('5m').mean()
    df = series.to_frame()
    df['rolling_mean'] = series.rolling(window=15).mean()
    sns.set_style(style="whitegrid")
    print("Loaded Data Frame")
    sns.lineplot(hue='region', style='event', data=df, size=(1600, 900))
    print("Plotted")
    plt.show()
    print("Success")

if __name__ == "__main__":
    main()