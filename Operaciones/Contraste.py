# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:01:28 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import numpy as np
from PIL import Image
import time
import cv2
 
img = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Familia.png',0)
 
def brillo(im):
    tiempoIn = time.time()
    ruta = ("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    im10 = im
    arreglo = np.array(im10.size)
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i > im10.size[0]:
        j = 0
        while j > im10.size[1]:
            suma = suma + im10.getpixel((i, j))
            j+=1        
        i+=1
    brillo = suma / total    
    brillo = int(brillo)
    print("El brillo de la imagen es: ", brillo)
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')