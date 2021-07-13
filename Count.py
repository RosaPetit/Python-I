# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:46:42 2021

@author: Rosa Petit
"""

#Uso de iteraciones y contadores.


data=[1,2,3]
total= 0
average=0
n=0
for value in data:
    n += 1  # += es la iteracion, el contador comienza desde 0 y va sumandado 1 en uno 
    total += value # aqui += ya comienza con los valores de la data no en 0
    average=total/n
    print("average:", average)