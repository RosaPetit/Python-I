#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image, ImageDraw 

#Tranformaciones geometricas (crea,rota,escala)

#crea una imagen 

img=Image.new("RGB",(150,250),(460,210,250))
 
dibujo=ImageDraw.Draw(img)
dibujo.line((100,100,200,200))

dibujo.line([10,10,10,35,90,100,150,180])

dibujo.polygon([100,150,130,165,150,200,100,280], fill=(255,0,0), outline=(255,0,0))
img.show()
