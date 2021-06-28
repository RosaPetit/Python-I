#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#importan las librerias  PIL

from PIL import Image, ImageDraw 
from PIL import ImageFont


# Dibujar Imagen 

img=Image.new("RGB",(350,350),(460,210,250))
 
dibujo=ImageDraw.Draw(img)
dibujo.line((100,100,200,200))


#Dibujar una linea
dibujo.line([10,10,10,35,90,100,150,180])


#Dibujar un poligono
dibujo.polygon([100,100,130,165,150,200,100,280], fill=(255,0,0), outline=(255,0,0))


#Agregar texto y Cambiar letra (para cambiar la letra se va a esta carpeta: /usr/share/fonts/liberation/)

letra=ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Italic.ttf",44)
dibujo.text((50,30),"Hello world!",font=letra) 



#Dibujar imagen
img.show()
