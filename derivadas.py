'''Programa para calcular derivadas'''

import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0.001,0.5,500)
x0 = 1
fx = np.exp(-x0)
fxx =-np.exp(-x0)
#Creamos los vectores vacios:
de1=[]
de2=[]
de3=[]



for i in h:
  # ciclo For para obtener las derivadas, el de1.append es para añadir los valores dentro del parentesis al vector vacio creado antes
  
  de1.append(  abs(( (np.exp(-(x0+i))-fx)/i) - fxx)  )
  de2.append(  abs(( (fx-np.exp(-(x0-i)))/i)- fxx) )
  de3.append(  abs(( (np.exp(-(x0+i)) - np.exp(-(x0-i))) /(2*i))-fxx) )


plt.plot(h,de1,"r")
plt.plot(h,de2,"b")
plt.plot(h,de3,"g")

plt.show()
