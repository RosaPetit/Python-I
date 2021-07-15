#!/usr/bin/env python2.6
#_*_coding: utf8_*_ 

from math import *

from math import sqrt
 
def __main__():
    print '''
    Ecuaciones de 2do. Grado
        ax^2 + bx + c = 0
          '''
    a = input('Coeficiente de A: ')
    b = input('Coeficiente de B: ')
    c = input('Coeficiente de C: ')
 
    try:
        # Si el discriminante es menor que cero, el resultado es imaginario.
        if ( b ** 2 - 4*a*c ) < 0:
            r = -b / (2.0*a)
            i = (sqrt(-(b ** 2 - 4*a*c)))/(2*a)
            print '''
            Solución:
 
            X (+): %f + %f
            X (-): %f - %f
            ''' % (r,i,r,i)
        # En caso contrario, el resultado es real.
        else:
            (X1,X2) = (-b + sqrt(b ** 2 - 4*a*c))/(2*a),(-b - sqrt(b ** 2 - 4*a*c))/(2*a)
            print '''
            Solución:
 
            X (+) %f
            X (-) %f
              ''' % (X1,X2)
 
    except:
        print '\n Ha ocurrido un error'
 
 
if __name__ == "__main__":
    __main__()
