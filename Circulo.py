#_*_coding: utf-8_*_

"Este es un programa basico que crea una ventana con las librerias Tkinter"

#llamo al modulo Tkinter
import Tkinter as Tki

#Creo una ventana
ventana = Tki.Tk()


#Creo el lienzo y defino el ancho y el largo de la ventana en pixeles
#Ancho
W = 400
#Altura
H = 300
lienzo = Tki.Canvas(ventana, width= W, height= H)
lienzo.pack()


#Dibujo una elipse
x0 = 100
y0 = 100
x1 = 300
y1 = 300
lienzo.create_oval(x0,y0,x1,y1, fill = "blue")


alto = 0
while alto<20:
	lienzo.move("pelota ", 5, 6)
	ienzo.after(10)
	lienzo.update()

#Esto es necesario para dibujar la ventana
ventana.mainloop()
