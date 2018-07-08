set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M:%S"
set style data lines
plot '../logs/log.oZ-angle.2015-01-01.csv' using 1:2 title 'oZ angle'
pause -1 "Hit any key to continue"