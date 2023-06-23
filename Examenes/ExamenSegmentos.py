# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:48:41 2021

Alumno: Antonio Alberto de la Luz Perez Rodriguez
"""
from PIL import Image
import scipy.misc
import numpy as np
import statistics
import random
import scipy
import time

def blanco_negro(im,grisBase):
    tiempoIn = time.time()
    ruta = ("C:/Users/CkriZz/Pictures/" + im)
    im = Image.open(ruta)
    im.show()
    im6 = im
    i = 0
    while i < im6.size[0]:
        j = 0
        while j < im6.size[1]:
            r, g, b = im6.getpixel((i, j))
            gris = (r + g + b) / 3
            if gris < grisBase:
                im6.putpixel((i, j), (0, 0, 0))
            else:
                im6.putpixel((i, j), (255, 255, 255))   
            j+=1
        i+=1
    im6.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos') 