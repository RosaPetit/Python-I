#!/usr/bin/env python
# -*- coding: utf8 -*- 

"Comentario"
import numpy as np 
import matplotlib

matplotlib.use("TKAgg")
import matplotlib.pyplot as plt

fig = plt.figure()

Agra = fig.add_subplot(111)
Agra.plot([],[]) #se grafica algo vacio
Agra.grid()

###############################
N = range(0,10)
tvec = np.linspace(0,2*np.pi, 50)
Agra.plot(tvec, np.sin(tvec))
Agra.set_ylim(-1.3, 1.3)
###############################


def Fac(n):#calculra el factorial de n
	A = n-1
	while(A>1):
		n = n*A
		A -= 1 #tomo el valor de A y le quito 1, x eso esta el menos(-)
	return n
# Corriendo el programa a mano, asignando el valores
# n=4 entonces A=3
# si A>1 
# n= n*A= (4)*(3) =12
# entonces A -=1 es A=2
#retorno a n
# n = n*A = (12)*(2)
# entonces A -=1 es A=1
# y asi sucesivamente....
	

def termT(tvec, i):#calculo de los terminos de la serie de Taylor
	e = (2*i) + 1
	f = Fac((2*i)+1)# factorial de numeros impares
	result = (tvec**(e)/f)
	return result

def animacion():
	taylor = np.zeros(len(tvec))
	for i in N:
		print i
		raw_input() #ejecuta el programa
		c = (-1)**i #alternar el signo
		taylor += c*termT(tvec, i)#suma cada termino de la serie
		Agra.plot(tvec, taylor)
		Agra.set_xlim(0, 2*np.pi)
		Agra.set_ylim(-1.3,1.3) #slep(0.5) quiere decir q cada medio segundo ejecutara la grafica
		fig.canvas.draw() # re-dibuja

#esto siempre se coloca para cuando necesitemos librerias graficas para animaciones, ya que python no la tiene incorporada
win = fig.canvas.manager.window
fig.canvas.manager.window.after(10, animacion) #canvas significa lienzo

plt.show()






