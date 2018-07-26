import pandas as pd

current = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/meter/processed/2018-07-20.tilt-from-vertical.10T.csv', header=0, parse_dates=True, index_col=0)
predicted = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/imported/2018-07-20.9447814.tides.csv', header=0, parse_dates=True, index_col=0)

result = current.join(predicted, how='outer')
result.to_csv('/home/max/projects/mukilteo-pnwdiving-org/data/reports/2018-07-20.tilt-from-vertical.10T..9447814.tides.csv')