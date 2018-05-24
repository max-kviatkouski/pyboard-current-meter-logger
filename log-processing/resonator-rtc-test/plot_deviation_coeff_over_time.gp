set xlabel "Seconds since PyBoard/PC clock sync"
show xlabel
set yrange [1: 1.1]
show yrange
plot filename using (15 * $0):1 title "Lag coefficient over time" with lines
pause -1 "Hit any key to continue"
