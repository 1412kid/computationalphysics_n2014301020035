#!/usr/bin/env gnuplot

set term epslatex standalone solid color size 12,4
set output "df2d.tex"
set multiplot layout 1,3

set title "Diffusion in two dimension" offset 0,-4
set zlabel "density $\\rho$" rotate by 90
set xtics ("-40" 10, "-20" 30, "0" 50, "20" 70, "40" 90)
set ytics ("-40" 10, "-20" 30, "0" 50, "20" 70, "40" 90)
set xyplane 0.0
# set zrange [0.0:0.01]
set key at 30,250
splot "d2t050.txt" matrix t "t=50" w p pt 3

set title "Diffusion in two dimension" offset 0, -4
set zlabel "density $\\rho$" rotate by 90
# set zrange [0.0:0.005]
splot "d2t100.txt" matrix t "t=100"  w p pt 6

set title "Diffusion in two dimension" offset 0,-4
set zlabel "density $\\rho$" rotate by 90
set xyplane 0.0
# set zrange [0.0:0.0025]
splot "d2t200.txt" matrix t "t=200"  w p pt 9

unset multiplot
set output
!xelatex df2d.tex &>/dev/null
!evince df2d.pdf &>/dev/null &
