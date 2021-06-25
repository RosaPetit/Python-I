#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image 

#Tranformaciones geometricas (crea,rota,escala)

#crea una imagen 

img=Image.new("RGB",(150,250),(460,210,250)) #tipo , largo, ancho y color

#Rotacion 

#img2=img.rotate(30)

#img2=img.rotate(30, (expand=True))

#Escal de imagen

img3=img.resize((400,500))

img3.show ()

