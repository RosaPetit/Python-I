#!/usr/bin/env python2.6
#_*_coding:utf8_*_

import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



fig=plt.figure()
ax=fig.add_subplot(111)
Proyectil,=ax.plot([],[])
Proyectil1,=ax.plot([],[],"r--")
ax.grid()

# Condiciones iniciales



tao=0.02
k= 0.035
m= 0.145

#Variables

xo1=eval (input("Introducir la posicion inicial en Xo de la particula:"))
yo1=eval (input("Introducir la posicion Inicial en Yo de la particula:"))
v=eval (input("Introducir el modulo de la velicidad de la particula:"))
b= eval (input("Introducir el valor  del angulo con respecto a a la horizontal:"))



def vox(v,b):
	vox=v*np.cos((b*np.pi)/180)
	return vox 

def voy(v,b):
	voy=v*np.sin((b*np.pi)/180)
	return voy
	

def acelerax (v, vox,k,b):
	ax=((-k)*v*(vox))
	return ax


def aceleray (v, voy,k,b):
	ay=((-k)*v*(voy))-(9.8)
	return ay



def animacion():
	xo=xo1
	yo=yo1

	xos=xo1
	yos=yo1

	vx=vox(v,b)
	vy=voy(v,b)

	vxs=vox(v,b)
	vys=voy(v,b)

	x=[]
	y=[]

	xs=[]
	ys=[]

	N=-0.05
	
	while (N<0):

		#Euler con roce

		vo= np.sqrt(vx**2+vy**2)
		vyn=(vy)+(tao*(aceleray (vo, vy,k,b)))
		vxn=(vx)+(tao*(acelerax (vo, vx,k,b)))
		xn=xo + (tao*vxn)
		yn=yo + (tao*vyn)
			
		x.append(xn)
       	y.append(yn)
		
		xo=xn		
		yo=yn
		vy=vyn
		vx=vxn

		Proyectil.set_data(x,y)
		#if(yn<0):
		#	N=0
		ax.set_xlim(0,70)
		ax.set_ylim(0,50)



		#Euler sin roce

		
		vym= vys - ((9.8)*tao) 
		vxm= vxs - ((9.8)*tao)
		xm= xos + (tao*vxm)
		ym= yos + (tao*vym)
		
		xs.append(xm)
       		ys.append(ym)

		xos=xm
		yos=ym
		vys=vym
		

		Proyectil1.set_data(xs,ys)


		#ax.set_xlim(np.amin(xs)-5,np.amax(xs)+5)
		#ax.set_ylim(np.amin(ys)-5,np.amax(ys)+5)

		ax.set_xlim(0,70)
		ax.set_ylim(0,50)
		
		if (ym<0):
			N=0


		fig.canvas.draw()#redibuja

win= fig.canvas.manager.window
fig.canvas.manager.window.after( 0,animacion)
plt.show()
fig.canvas.draw()

	



