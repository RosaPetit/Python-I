#!/usr/bin/env python2.6
#_*_coding: utf8_*_ 

from math import *


formul= raw_input ("escriba una fórmula que tenga como variable x:")
x= eval(raw_input("Introduzca x: "))
for x in range(0,20):
	res = eval(formul)
	print '%s para x = %g da %g'% (formul, x, res)
