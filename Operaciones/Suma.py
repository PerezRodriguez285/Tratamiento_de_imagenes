# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:06:12 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar funciones OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import cv2
#import numpy as np
#import matplotlib.pyplot as plt
import time
from PIL import Image

def suma(im, alpha):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    im12 = im
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            valor = im12.getpixel((i, j))            
            valor = valor + alpha
            if valor >= 255:
                valor = 255
            else:
                valor = valor
            im12.putpixel((i, j),(valor))
            j+=1
        i+=1
    im12.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos') 


def multiplicacion(im, alpha):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    im12 = im
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            valor = im12.getpixel((i, j))            
            valor = valor * alpha
            if valor >= 255:
                valor = 255
            if valor <= 0:
                valor = valor
            im12.putpixel((i, j),(valor))
            j+=1
        i+=1
    im12.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos') 
     
    
def abrir_imagen():
    imagen = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png",0) 
    cv2.imshow("Prueba de imagen", imagen)
    cv2.waitKey(0)
    cv2.imwrite("lena2.png", imagen)
    cv2.destroyAllWindows()