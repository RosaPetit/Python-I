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

#####variables####
N = range(0,10)
tvec = np.linspace(0,2*np.pi,50)
ax.plot(tvec,np.sin(tvec))
ax.set_ylim(-1.3,1.3)
##########

def Fac(n):#Calcula el factorial de n
         a = n-1
         while(a>1):
             n = n*a
             a-= 1 #le quita 1 a "a"
         return n

def termT(tvec,i):#calcula los t\303\251rminos de la serie de Taylor
      e = (2*i)+1
      f = Fac((2*i)+1)
      result = (tvec**(e)/f)
      return result

def animacion():
      taylor = np.zeros(len(tvec))#arreglo de puros ceros del largo te tevec
      for i in N:
                print i
                #raw_input()
                c=(-1)**i#alterna el signo
                taylor += c*termT(tvec,i)#suma cada t\303\251rmino de la serie
                ax.plot(tvec,taylor)
                ax.set_xlim(0,2*np.pi)
                ax.set_ylim(-1.3,1.3)#rangos de x e y
                sleep(0.5)#se muestra cada 5 segundos
                fig.canvas.draw()#redibuja

win= fig.canvas.manager.window
fig.canvas.manager.window.after(10,animacion)
plt.show()


