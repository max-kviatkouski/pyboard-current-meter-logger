set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M:%S"
set style data lines
plot '~/projects/pyboard-current-meter-logger-data/log.2018-07-20.50-average.csv' using 1:2 title 'oZ angle'
pause -1 "Hit any key to continue"
