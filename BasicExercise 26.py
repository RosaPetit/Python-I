#!/usr/bin/env python2.6
#_*_coding:utf8_*_

#Ser importan las librerias  PIL

from PIL import Image 

# Se importa la libreri numerica para tratar con la matriz de RGB


import numpy as np

#Importar imagen

img= Image.open("/home/rpetit/Python/figura.jpg.eps")

print img.mode


# Para cponvertir la imangen a RBJ
img2=img.convert("RGB")

#Para usar una matris 

ro,ve,az=img2.split()

#Se convierte la barra ro en un arreglo

datos_ro=np.array(ro.getdata())

print type(datos_ro)
print datos_ro.size
print datos_ro.shape
print datos_ro
print ro

#Formando la matriz original  (dimenciones en x=213 y en y=159)

print img2.size
datos_ro_matriz= datos_ro.reshape(159,213)

#Confirmacion de dtos 
print datos_ro_matriz.size

# Para poder trabajar con las matrices de guardan las dimensiones en una variable

(x,y)=datos_ro_matriz.shape
datos_ro_matriz[: , (y/2)-20:(y/2)+20]=122*np.ones((x,40))

# Se forma un nuevo vectotor para convertir la banda ro para convertirla en un vector del tamano delas x y y

nuevo_ro= datos_ro_matriz.reshape(x*y)
ro.putdata(nuevo_ro)

nueva_img2=Image.merge("RGB",(ro,ve,az))

nueva_img2.show()
