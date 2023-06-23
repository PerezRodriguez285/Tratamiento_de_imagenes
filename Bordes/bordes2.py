# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:15:15 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Bordes con OpenCV
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
Descripción: 
"""

import numpy as np
import cv2
 
#Cargamos una fuente de texto
font = cv2.FONT_HERSHEY_SIMPLEX
 
#Abrimos la imagen
imagen = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg')
if(imagen is None):
    print("Error: no se ha podido encontrar la imagen")
    quit()
 
#Convertimos la imagen a HSV
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Extraemos el fondo verde
verde_bajos = np.array([50,1,1])
verde_altos = np.array([100, 254, 254])
fondo = cv2.inRange(hsv, verde_bajos, verde_altos)
 
#Invertimos la mascara para obtener las bolas
bolas = cv2.bitwise_not(fondo)
 
 
#Eliminamos ruido
kernel = np.ones((3,3),np.uint8)
bolas = cv2.morphologyEx(bolas,cv2.MORPH_OPEN,kernel)
bolas = cv2.morphologyEx(bolas,cv2.MORPH_CLOSE,kernel)
 
 
#Buscamos los contornos de las bolas y los dibujamos en verde
contours,_ = cv2.findContours(bolas, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contours, -1, (0,255,0), 2)
 
#Buscamos el centro de las bolas y lo pintamos en rojo
for i in contours:
    #Calcular el centro a partir de los momentos
    momentos = cv2.moments(i)
    cx = int(momentos['m10']/momentos['m00'])
    cy = int(momentos['m01']/momentos['m00'])
 
    #Dibujar el centro
    cv2.circle(imagen,(cx, cy), 3, (0,0,255), -1)
 
    #Escribimos las coordenadas del centro
    cv2.putText(imagen,"(x: " + str(cx) + ", y: " + str(cy) + ")",(cx+10,cy+10), font, 0.5,(255,255,255),1)
 
#Mostramos la imagen final
cv2.imshow('Final', imagen)
  
#Salir con ESC
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
#Destruir la ventana y salir
cv2.destroyAllWindows()
quit()
