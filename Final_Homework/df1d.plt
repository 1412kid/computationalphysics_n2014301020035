#!/usr/bin/env gnuplot

set term epslatex standalone solid color size 12,3
set output "df1d.tex"
set multiplot layout 1,3

set title "Diffusion in one dimension" offset 0,-1
set ylabel "density $\\rho$" rotate by 90
# set yrange [0.0:0.01]
set key at 30,250
plot "t.txt"  u ($1-100):3  w lp pt 3 t ""

set title "Diffusion in one dimension" offset 0, -1
set ylabel "density $\\rho$" rotate by 90
# set yrange [0.0:0.005]
plot "t.txt" u ($1-100):4  w lp pt 6 t ""

set title "Diffusion in one dimension" offset 0,-1
set ylabel "density $\\rho$" rotate by 90
# set yrange [0.0:0.0025]
plot "t.txt" u ($1-100):5  w lp pt 9 t ""

unset multiplot
set output
!xelatex df1d.tex &>/dev/null
!evince df1d.pdf &>/dev/null &
