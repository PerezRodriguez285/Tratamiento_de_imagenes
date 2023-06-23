# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:58:42 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
		   Luis Angel Diaz Navas
           Miguel Angel Flores Urbina
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img1 = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/lc2.tiff')
 
#Genera el historama de la imagen
hist,bins = np.histogram(img1.flatten(),256,[0,256])
 
#Genera la función de distribución acumulada (cdf por sus siglas en inglés)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
 
#Genera los gráficos del histograma y de la función de distribución acumulada
plt.plot(cdf_normalized, color = 'b')
plt.hist(img1.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper right')
plt.show()

cdf_m = np.ma.masked_equal(cdf,0) 
 
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
 
#Rellena los valores previamente enmascarados con ceros
cdf = np.ma.filled(cdf_m,0).astype('uint8')
 
#Aplica la ecualización a los píxeles de la imagen original
img2 = cdf[img1]
 
#Grafica la imagen resultante de aplicar la ecualización del histograma
cv2.imshow('imagen',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
hist,bins = np.histogram(img2.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper right')
plt.show()