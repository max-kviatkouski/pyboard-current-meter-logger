import pandas as pd

day = '2018-12-24'
#TODO: fix merging code
current = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/meter/processed/{}.tilt-from-vertical.10T.csv'.format(day), header=0, parse_dates=True, index_col=0)
predicted = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/imported/{}.tides.csv'.format(day), header=0, parse_dates=True, index_col=0)

result = predicted.join(current, how='outer')
result.to_csv('/home/max/projects/mukilteo-pnwdiving-org/data/reports/{}.csv'.format(day))