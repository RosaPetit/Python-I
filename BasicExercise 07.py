#!/usr/bin/env python2.6
#_*_coding: utf8_*_ 

from math import *
import os

# modulo de sistema operativo (import os)

nombre_sal= raw_input("Escriba el nombre del archivo de salida: ")
nombre_ent= raw_input("Escriba el nombre del archivo de entrada: ")

try:
	archi_sal= open(nombre_sal, "w")
except IOError:
	print "El archivo" + nombre_sal + "no se pudo abrir"

try:
	archi_ent= open(nombre_ent, "r")
except IOError:
	print "El archivo" + nombre_ent + "no se pudo abrir"



# try (es intentar en este caso un programa)
# except (si no lo congue aprarece lo que aparece en print)

for lin in archi_ent:
	xy= lin.split() # corta el arreglo es decir lo  divide
	x= float(xy[0])
	y= float(xy[1])
	yy= sin(y)**3
	archi_sal.write("%s\t%g\n" %(x,yy) )


archi_sal.close()
archi_ent.close()

