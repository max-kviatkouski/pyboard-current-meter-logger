set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set style data lines
plot '../logs/log.averaged_accel.2015-01-01.csv' using 1:2 title 'X', '' using 1:3 title 'Y', '' using 1:4 title 'Z'
pause -1 "Hit any key to continue"