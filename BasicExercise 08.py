#!/usr/bin/env python2.6
#_*_coding:utf8_*_
import numpy as np
import matplotlib.pyplot as plt
#Programa que calcula el campo electrico

#constantes
q = 12*10**(-9) 
e = 8.8541878*10**(-12)
K = 1/(4*np.pi*e)

#vector x

x = np.linspace(-0.5,0.5,250)
y = np.linspace(-0.5,0.5,250)
#vector constante
a = 0.02*np.ones(250)

campo1 = ((1/8*a**2)+(1/8*a**2)
campo2 = (np.sqrt( (a-x)**2+a**2))**3

A = ((a+x)/rmas3)+((a-x)/rmen3)
B = (a/rmas3)-(a/rmen3)
#calculo de modulo de E
Ey= K*q*np.sqrt(A**2+B**2)

#GRAFICACI\303\223N
plt.plot(x,E)
plt.show()



