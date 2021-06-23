#!/usr/bin/env python2.6
#_*_coding:utf8_*_
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


from time import sleep
#para no presionar enter la pc lo hacecada cierto tiempo
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot([],[])
ax.grid()

# variables

N= range(0,10)
tvec= np.linspace(0,2*np.pi,50)
ax.plot(tvec, np.sin(tvec))
ax.set_ylim(-1.3, 1.3)

#

def Fac(n): # calcula el factorial de n
	a= n-1
	while(a>1):
		n=n*a
		a-=1 
	return n

def termT(tvec, i): # calcula los terminos de la serie de taylor
	e= (2*i)+1
	f= Fac((2+i)+1)
	result= (tvec**(e)/f)
	return result

def animacion():
	taylor= np.zeros(len(tvec))
	for i in N:
		print i
		#raw_input()
		c= (-1)**i #alterna el signo
		taylor += c*termT(tvec, i) # suma de cada termino de la serie
		ax.set_xlim(0, 2*np.pi)
		ax.set_ylim(-1.3, 1.3)
		fig.canvas.draw() # re-dibuja
		

win= fig.canvas.manager.window
fig.canvas.manager.window.after(10, animacion)

plt.show()

