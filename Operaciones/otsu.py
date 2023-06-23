# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:46:45 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar funciones OPENCV
Alumno:  Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import time

def otsu(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    width, height = ima.size
    img = np.array(ima.getdata())
    histogram = np.array(ima.histogram(),float) / (width * height)
    #Vector de probabilidad acomulada.
    omega = np.zeros(256)
    #Vector de media acomulada
    mean = np.zeros(256)
    #Partiendo del histograma normalizado se calculan la probabilidad
    #acomulada (omega) y la media acomulada (mean)
    omega[0] = histogram[0]
    for i in range(len(histogram)):
        omega[i] = omega[i - 1] + histogram[i]
        mean[i] = mean[i - 1] + (i - 1) * histogram[i]
    sigmaB2 = 0
    mt = mean[len(histogram) - 1] #El Valor de la intensidad media de la imagen
    sigmaB2max = 0
    T = 0
    for i in range(len(histogram)):
        clase1 = omega[i]
        clase2 = 1 - clase1
        if clase1 != 0 and clase2 != 0:
            m1 = mean[i] / clase1
            m2 = (mt - mean[i]) / clase2
            sigmaB2 = (clase1 * (m1 - mt) * (m1 - mt) + clase2 * (m2 - mt) * (m2 - mt))
            if sigmaB2 > sigmaB2max:
                sigmaB2max = sigmaB2
                T = i
    thr = int(T)
    print('El Umbral Optimo De La Imagen Es: ' ,thr)
    #Se Aplica la umbralización al "array" de la imagen
    #limites de procesado en x
    x_min, x_max = 0, width
    #limites de procesado en y
    y_min, y_max = 0, height
    #imagen de salida
    img_out = np.zeros(width * height)
    #procesado de la imagen
    loc = 0 #posicin del "pixel" actual
    for y in range (y_min, y_max):
        for x in range(x_min, x_max):
            loc = y * width + x
            if img[loc] > thr:
                img_out[loc] = 255
            else:
                img_out[loc] = 0
    img_thr = img_out
    im_otsu = img_thr.reshape(height, width)
    im_otsu = Image.fromarray(im_otsu)
    im_otsu.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
