#!/usr/bin/env python2.6
#_*_coding:utf8_*_


"Este es un programa basico que crea una ventana con las librerias Tkinter"

#llamo al modulo Tkinter
import Tkinter as Tki

#Creo una ventana
ventana = Tki.Tk()


#Creo el lienzo y defino el ancho y el largo de la ventana en pixeles



#Ancho
W = 500
#Altura
H = 500
lienzo = Tki.Canvas(ventana, width= W, height= H)
lienzo.pack()





#Dibujo una elipse
x0 = 200
y0 = 100
x1 = 150
y1 = 150

xn=200
xm=100
yn=150
ym=150

	
lienzo.create_oval(x0,y0,x1,y1, fill = "green", tag = "pelota")
lienzo.create_rectangle(x0+5,y0-5,x1+5,y1-5, fill = "black", tag = "cuadrado")
lienzo.create_oval(xn+20,yn-50,xm-50,yn, fill = "pink", tag = "pelota1")



deltax = 1
deltay = 1
deltan = 1
deltam = 1
alto = True

while alto:
	lienzo.move("pelota", deltax, deltay)
	xx0,yy0,xx1,yy1= lienzo.bbox("pelota")
	xxn,yyn,xxm,yym= lienzo.bbox("cuadrado")	

	if(yy1>=H):
	lienzo.coords("pelota",xx1,yy0,xx0,0)
	
	if(yy0<=0):
	lienzo.coords("pelota",xx1,yy0,xx0,H+5)
	
	if(xx1>=W):
	lienzo.coords("pelota",0,yy0,xx0,yy1)
	
	if(xx0<=0):
	lienzo.coords("pelota",xx1,yy0,xx0,W+5)	


	

	lienzo.after(20)
	lienzo.update()



#Esto es necesario para dibujar la ventana
ventana.mainloop()
