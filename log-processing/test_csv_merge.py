from datetime import datetime

day = '2019-01-14'
#TODO: fix merging code
current_filename = '/home/max/projects/mukilteo-pnwdiving-org/data/meter/processed/{}.tilt-from-vertical.10T.csv'.format(day)
predicted_filename = '/home/max/projects/mukilteo-pnwdiving-org/data/imported/{}.tides.csv'.format(day)
# current = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/meter/processed/{}.tilt-from-vertical.10T.csv'.format(day), header=0, parse_dates=True, index_col=0)
# predicted = pd.DataFrame.from_csv('/home/max/projects/mukilteo-pnwdiving-org/data/imported/{}.tides.csv'.format(day), header=0, parse_dates=True, index_col=0)

with open(current_filename) as c:
    current_lines = c.readlines()

with open(predicted_filename) as p:
    predicted_lines = p.readlines()

#no headers on predicted (tides from NOAA)
#need to add extra comma to lines containing meter angle (current lines)
map = dict()
for cl in current_lines[1:]:
    t = datetime.strptime(cl.split(',')[0], '%Y-%m-%d %H:%M:%S')
    map[t] = cl.strip() + ','

for pl in predicted_lines:
    t = datetime.strptime(pl.split(',')[0], '%Y-%m-%d %H:%M')
    map[t] = pl.strip()

with open('/home/max/projects/mukilteo-pnwdiving-org/data/reports/{}.csv'.format(day), 'w+') as r:
    r.write('Time,Meter Tilt (in degrees),Tide (in ft)\n')
    for key in sorted(map.keys()):
        r.write(map[key]+'\n')

# result = predicted.join(current, how='outer')
# result.to_csv('/home/max/projects/mukilteo-pnwdiving-org/data/reports/{}.csv'.format(day))