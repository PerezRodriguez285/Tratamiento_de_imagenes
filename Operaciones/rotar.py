# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 07:42:34 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""


import numpy as np
import cv2
import math
from scipy import ndimage
from PIL import Image

img = Image.open('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png')
nueva_img = img.resize((256,256))

img = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png')

cv2.imshow("Imagen original", img)    
key = cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

# en este arrelo se agregan los angulos
angulos = [] #ejemplo angulo[90]

for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angulo = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angulos.append(angulo)

median_angle = np.median(angulos)
img_rotated = ndimage.rotate(img, median_angle)

cv2.imwrite('Lena90.png', img_rotated)
nueva_img.save('Lenna.png','png')