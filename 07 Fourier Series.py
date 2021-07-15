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


#variables1
n = range(0,10)
tvec = np.linspace(-np.pi,-np.pi/2,500)
ax.set_ylim(-2,-1)
 

#variables2

tved = np.linspace(-np.pi/2,0,500)
ax.set_ylim(-1,0)
 
#variables3

tvee = np.linspace(0,np.pi/2,500)
ax.set_ylim(0,1)


#variables4

tvef = np.linspace(np.pi/2,np.pi,500)
ax.set_ylim(1,2)


#def termP(j):
#	f= 2*j
#	result=(2/(f*np.pi))
#	return result

def termT(i):
      f = ((2*i)+1)
      result = (2/(f*np.pi))
      return result


def animacion():
      four = np.zeros(len(tvec))
      for i in n:
                print i
                
		#four +=	termP(j)*np.cos((2*j)*tvee*tvef)
                four += termT(i)*np.sin(((2*i)+1)*tvec*tevd)#suma cada termino de la serie
                ax.plot(tvec,four)
                ax.set_xlim(-3.5,3.5)
                ax.set_ylim(-1.5,1.5)#rangos de x e y
                sleep(0.5)#se muestra cada 5 segundos
                fig.canvas.draw()#redibuja

win= fig.canvas.manager.window
fig.canvas.manager.window.after(10,animacion)
plt.show()



