# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:05:09 2021

@author: MI PC
"""

import numpy as np
import cv2
import math
from scipy import ndimage
from PIL import Image

img = Image.open('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/patos.png')
nueva_img = img.resize((256,256))

img = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/patos.png')

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

cv2.imwrite('patos90.png', img_rotated)
nueva_img.save('Patos pequeños.png','png')