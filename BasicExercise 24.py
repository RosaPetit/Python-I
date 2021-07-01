#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image 


#Importar imagen

img= Image.open("/home/rpetit/Python/figura.jpg.eps")
#img= Image.open("/home/rpetit/Imagenes/roe.jpg")

print img.mode

# Para cponvertir la imangen a RBJ
img2=img.convert("RGB")

#Para usar una matris

ro,ve,az=img.split()
print ro
#print ro.mode, ve.mode, az.mode

ro.show ()
ve.show ()
az.show ()
#img.show()
