#!/usr/bin/env python2.6
#_*_coding:utf8_*_
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


#constantes
c=0.35
d=0.024
m=0.145
A=np.pi*(d**2/4)
K=0.1  #(c*A)/(2*m)

#condiciones iniciales
x=0
y=0
vix=100
viy=120
#CONSTANTE DE TIEMPO
T=0.05
vx=vix
vy=viy

fig=plt.figure()
ax=fig.add_subplot(111)
l, =ax.plot([],[])
ax.grid()

             

         
def animacion():
      x=0
      y=0
      vix=100
      viy=120
      #CONSTANTE DE TIEMPO
      T=0.05
      vx=vix
      vy=viy
      con=-0.5
      r=[]
      t=[]
      while (con<0):
             r.append(x)
             t.append(y)
             b2=vx**2+vy**2
             x=x+(T*vx)#posicion x
             y=y+(T*vy)#posicion y
             vx=vx-(T*K*np.sqrt(b2)*vx)#velocidad x
             
             vy=vy-(T*K*np.sqrt(b2)*vy)-(T*9.8)#velocidad y
             
             
             
             l.set_data(r,t)
             if (y<0):
                  con=1
             ax.set_xlim(-1,70)
             ax.set_ylim(0,51)#rangos de x e y
             print x,y

             
             #ax.plot(vx,vy)
             fig.canvas.draw()#redibuja


win= fig.canvas.manager.window
fig.canvas.manager.window.after(0,animacion)
plt.show()
fig.canvas.draw()
