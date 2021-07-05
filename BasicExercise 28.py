#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image 

#Tranformaciones geometricas (crea,rota,escala)

img= Image.open("/home/rpetit/Imagenes/manut.png")


#Rotacion 

img2=img.rotate(30)

#img2=img.rotate(30, (expand=True))

#Escal de imagen

#img3=img.resize((400,500))

#Interpolacion cuando de una imagen

#img4=img.resize((400,500),Image.ANTIALIAS)

img2.show ()
img.show()
