set title "Titulo opcional de la grafica"
set xlabel "tiempo"
set ylabel "{/Symbol t} r c^{3}"

set format y "10^{%l}"


# Primera grafica se usa plot
clear

plot "ClaArc1"  using 1:2:3 w xerrorbars

# parametros de error entre graficas
# Para especificar las columnas using 1:2:4
# w xerrorbars & w yerrorbars es para agregar los errores en x & y en la grafica cuando el error es igual (los datos hay que colocarlos en el orden correcto)


# Segunda grafica se usa replot

a=5
b=-0.3
f(x)=(a*x)+b
fit f(x) "ClaArc1" via a,b
replot f(x) title "Nombre de la funcion" w l 1
print a



# 24 Numero de letra
# Para ejecutar (gnuplot nombre de archivo)

set terminal postscript eps enhanced 24
set out "figura.eps"


replot 

