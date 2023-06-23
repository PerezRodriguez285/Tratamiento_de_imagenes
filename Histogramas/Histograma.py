# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:56:50 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Histograma de una imagen
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

img =cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/cameraman.png",0)
intensidades = []
for i in range(255):
    intensidades.append(0)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensidades[img.item(i,j)]=intensidades[img.item(i,j)]+1

intensidades = np.asarray(intensidades)
plt.plot(intensidades)
plt.show()
