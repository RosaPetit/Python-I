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


#variables
n = range(0,10)
tvec = np.linspace(-2*np.pi,2*np.pi,500)
#ax.plot(tvec,np.sin(tvec))
ax.set_ylim(1,-1)


def termT(i):
      f = ((2*i)+1)
      result = (4/(f*np.pi))
      return result

def animacion():
      four = np.zeros(len(tvec))
      for i in n:
                print i
                
                four += termT(i)*np.sin(((2*i)+1)*tvec)#suma cada t\303\251rmino de la serie
                ax.plot(tvec,four)
                ax.set_xlim(-2*np.pi,2*np.pi)
                ax.set_ylim(-1.3,1.3)#rangos de x e y
                sleep(0.5)#se muestra cada 5 segundos
                fig.canvas.draw()#redibuja

win= fig.canvas.manager.window
fig.canvas.manager.window.after(10,animacion)
plt.show()


