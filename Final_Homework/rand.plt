#!/usr/bin/env gnuplot

set term epslatex standalone solid color size 8,4
set output "rand1d.tex"
set title "$<x^2>$ of 10000 walks in one dimension"
set ylabel "$<x^2>$" rotate by 90
set xlabel "t"
plot "rand.txt" u 1:2 w p pt 4 t ""
set output
!xelatex rand1d.tex &>/dev/null


set term epslatex standalone solid color size 8,4
set output "rand2d.tex"
set title "$<x^2>$ of 10000 walks in two-dimension"
set ylabel "$<x^2>$" rotate by 90
set xlabel "t"
plot "rand.txt" u 1:3 w p pt 4 t ""
set output
!xelatex rand2d.tex &>/dev/null

set term epslatex standalone solid color size 8,4
set output "rand3d.tex"
set title "$<x^2>$ of 10000 walks in three-dimension"
set ylabel "$<x^2>$" rotate by 90
set xlabel "t"
plot "rand.txt" u 1:2 w p pt 4 t ""
set output
!xelatex rand3d.tex &>/dev/null
