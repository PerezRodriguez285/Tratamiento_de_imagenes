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

def segmentacion(im,grisBase):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    im7 = im
    i = 0
    while i < im7.size[0]:
        j = 0
        while j < im7.size[1]:
            r, g, b = im7.getpixel((i,j))
            gris = (r + g + b) / 3
            if gris < grisBase:
                im7.putpixel((i,j), (0,0,0))
            else:
                im7.putpixel((i,j), (255,255,255))
            j+=1
        i+=1
    im7.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')
