#!/usr/bin/env python2.6
#_*_coding: utf8_*_ 

from math import *
import os

nombre= raw_input ("Escriba el nombre del archivo de salida: ")
formul= raw_input ("Escriba una formula (la variables es x): ")


try:
	archiv = open (nombre, "r")

except IOError:
	print "El archivo no puedo abrirse"
	exit()

for x in range(0,25):
	resultado= eval (formul)
	archiv.write("%g \t%5.2g \n" %(x, resultado))

archiv.close()
