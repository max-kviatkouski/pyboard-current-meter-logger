set boxwidth 0.9 relative
set style data histograms
set style fill solid 1.0 border -1
set ylabel "Seconds"
show ylabel
set xrange[0:325]
plot filename using 1 title "Absolute error"
pause -1 "Hit any key to continue"
