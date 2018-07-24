import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def data_parser(dstring):
    s = dstring[0]
    d = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    return d

def main():
    dframe = pd.read_csv('../../../pyboard-current-meter-logger-data/log.fixed-time.2018-07-20.csv',
                         header=None, index_col=0)
    sns.set_style(style="whitegrid")
    print("Loaded Data Frame")
    sns.relplot(data=dframe, palette="tab10")
    print("Plotted")
    plt.show()
    print("Success")

if __name__ == "__main__":
    main()