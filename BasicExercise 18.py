#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image 

#Se guarda el archivo en una variable "im" (la variable puede cambiar)

im= Image.open("/home/rpetit/Imagenes/carita.png")

print im.size #Tamano de la imagen

print im.mode #Forma en que se guardo RGBA

print im.info # resolucion

print im.filename #Nombre de la imagen

#im.show ()

pedazo=(50,50,100,100)

region= im.crop(pedazo)

#region.show()

im.paste(region,(20,20))
im.show()
