#!/usr/bin/env python2.6
#_*_coding:utf8_*_


"""
comentarios y documentos
"""

import numpy as np
import matplotlib
import time
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

fig = plt.figure()
#figura1
a1= fig.add_subplot(111)
line1, = a1.plot([],[])
a1.grid()

#declaracion de variable
xn0=eval(raw_input("Introduzca el valor de xn:"))
yn0=eval(raw_input("Introduzca el valor de yn:"))
vo=eval(raw_input("Introduzca la amplitud en vo :"))
ta=eval(raw_input("Introduzca el valor del angulo  ta :"))
g=9.8
T=0.05
#definimos variables
VOvec=[vo*np.cos((ta*np.pi)/180) , (vo*np.sin((ta*np.pi)/180))]
vox , voy = VOvec
 


xn1=[]
yn1=[]
vyn=[]
vxn=[]

def calc_xn1(T):
        xn1=xn+T*vox
        return xn1

def calc_yn1(T):
        yn1=yn+T*voy
        return yn1

def calc_vyn(T):
        vyn=voy+T*g
        return vyn





def anima():
        yn=[]
        xn=[]
        v=[]
        H=[]
        g=9.8
        xn.append(xn0)
        yn.append(yn0)
        v.append(voy)
        i=1
        T=0.05
        t=T
        k=1
        H=((voy**2)/(2*g))+(yn)
        while (k>0):
                xn.append(xn0+vox*t)
                v.append(v[i-1]-T*g)
                yn.append(yn[i-1]+T*v[i])
            #grafica x vs y
                line1.set_data(xn,yn)
                a1.set_xlim(0,xn[len(xn)-1])
                a1.set_ylim(0,H)
                t=t+T
                i=i+1
                if (yn[i-1]<0):
                        k=0
                #time.sleep(0.1)
                fig.canvas.draw()
