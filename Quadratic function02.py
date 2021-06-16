from math import sqrt
import numpy

print "Este programa le ayudara a resolver ecuaciones de segundo grado de la forma ax**2+bx+c=0"
ejecutar=1
while ejecutar==1:	
	a=float(raw_input("introdusca el valor de a: "))
	b=float(raw_input("introdusca el valor de b: "))
	c=float(raw_input("introdusca el valor de c: "))
	print "la ecuacion es:",a,"x**2+",b,"x+",c,"=0"
	g=((b**2)-(4*a*c))
	if g<0:
		print "esta ecuacion no tiene una solucion dentro de los numeros reales"
	else:

		x1=((-b)+sqrt(g))/(2*a)
		x2=((-b)-sqrt(g))/(2*a)
		print "sus dos resultados son:",x1,x2
		if x1==x2:
			print "esta ecuacion cuadratica es un cuadrado perfecto"
		else:
			print "se puede completar el cuadrado de la siguiente forma:"
			k=(b/2*a)
			i=a*k**2
			j=c-i
			if k>0 or k==0:
				print a,"(x +",k,")**2+",i
			else:
				print a,"(x -",-k,")**2+",i
	print "si quiere resolver otra ecuacion presione 1"
	opcion=int(raw_input())
	if opcion==1:
		ejecutar=opcion
	else:
		print "hasta luego"
		ejecutar=0

