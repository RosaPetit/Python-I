set key Left spacing 1.5 

set xrange [-6:6]



f(x)= exp(x)*sin(x**2)/x**2
g(x)= cos(3*x)*(x**2)

set terminal epslatex color
set out "/home/rpetit/Gnuplot/figura2.eps"

plot f(x) title "$\\sqrt{\sen(\theta x)}/\log(x)$"
replot g(x) title "$\ x**3 + \cos(\alpha x**2) $" 


# el put para colocar el directorio de la figura
