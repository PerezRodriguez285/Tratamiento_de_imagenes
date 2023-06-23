# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:14:05 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
 
import numpy as np
import cv2

image = cv2.imread("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/ovnis.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Original",image)
cv2.waitKey()
 
sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)#x gradiente de dirección
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)#y gradiente de dirección
 
sobelX = np.uint8(np.absolute(sobelX))#x gradiente de dirección valor absoluto
sobelY = np.uint8(np.absolute(sobelY))#y valor absoluto del gradiente de dirección
 
sobelCombined = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.waitKey()
cv2.imshow("Sobel Y", sobelY)
cv2.waitKey()
cv2.imshow("Sobel Combinado", sobelCombined)
cv2.waitKey()



image1 = cv2.imread("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/ovnis.jpg")# Leer en imagen
image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Image",image1)#Mostrar imagen
cv2.waitKey()
 
canny = cv2.Canny(image1,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey()