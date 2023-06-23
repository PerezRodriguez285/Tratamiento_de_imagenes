# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:53:45 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
filename = "C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/"
str=filename+"/*.jpg"
mat=io.ImageCollection(str)
img=mat[0]
 ## Cree un detector MSER y detecte el área MSER de la imagen
 ## kpkp guarda el punto clave detectado
mser=cv2.MSER_create()
regions,boxes=mser.detectRegions(img)
kpkp=mser.detect(img)
print len(mser.detect(img))
 ## Use el cuadro rojo para enmarcar las áreas MSER detectadas, los cuadros guardan las coordenadas de la esquina superior izquierda de estas áreas y el ancho y alto del área
for i in range(len(boxes)):
    x,y,w,h=boxes[i]
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 # Crear un extractor de características SIFT
siftt=cv2.xfeatures2d.SIFT_create()
 
print len(regions)
print len(boxes)
kp=siftt.detect(img,None)
 ## Calcular el descriptor local de kpkp
des=siftt.compute(img,kpkp)
print len(des[0])
 ## Dibuje estos puntos clave en la imagen
cv2.drawKeypoints(img,kpkp,mat[0])
plt.imshow(mat[0])    