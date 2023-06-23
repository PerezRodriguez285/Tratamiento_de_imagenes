# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:16:36 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Bordes en una imagem
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
Descripción: 
"""
from PIL import Image
#import numpy as np
import time


def bordes(im, mask):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    [ren, col] = ima.size
    pix = ima.load()
    out_im = Image.new("L", (ren, col))
#    gx + gy + prewit45° = ([1,3,3],[-3,-2,3],[-3,-3,1])
#    gx = ([-1,0,1], [-2,0,2], [-1,0,1])
#    gy = ([1,2,1], [0,0,0], [-1,-2,-1])   
    out = out_im.load()
    for i in range(ren):
        for j in range(col):
            suma = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and m >= 0 and n < ren and m < col:
                        suma += mask[n - (i - 1)][ m - (j - 1)] * pix[n, m]
            out[i, j] = suma
    out_im.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')